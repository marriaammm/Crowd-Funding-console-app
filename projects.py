from datetime import datetime
from auth import get_current_user
from dependancies import load, save, PROJECTS_FILE
from validations import get_valid_float, get_valid_date, get_valid_float_optional 

def _select_user_project(action):
    all_projects = load(PROJECTS_FILE)
    mine = [p for p in all_projects if p['owner'] == get_current_user()['email']]
    if not mine:
        print(f"You have no projects to {action}.")
        return None,None
    print(f"\nYour projects:")
    for i, p in enumerate(mine, start=1):
        print(f"[{i}] {p['title']} ({p['start']} to {p['end']})")
    try:
        selected = int(input(f"Select a project to {action}: "))
        project = mine[selected - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return None     
    
    return project,all_projects


def create_project():
    user = get_current_user()
    if not user:
        print("You must be logged in to create a project.")
        return

    projects = load(PROJECTS_FILE)

    title = input("Project title: ").strip()
    details = input("Project description: ").strip()

    target = get_valid_float("Project amount: ")
    start_date = get_valid_date("Starting at (YYYY-MM-DD): ")
    end_date = get_valid_date("Ending at (YYYY-MM-DD): ", start_date)

    projects.append({
        "owner": user['email'],
        "title": title,
        "details": details,
        "target": target,
        "start": start_date.strftime("%Y-%m-%d"),
        "end": end_date.strftime("%Y-%m-%d")
    })
    save(PROJECTS_FILE, projects)
    print("Project created successfully.")


def list_projects():
    projects = load(PROJECTS_FILE)
    if not projects:
        print("No projects found.")
        return

    for i, p in enumerate(projects, start=1):
        print(f"\n[{i}] {p['title']} by {p['owner']}")
        print(f"Details: {p['details']}")
        print(f"Target: {p['target']} EGP")
        print(f"Duration: {p['start']} to {p['end']}")

def edit_project():
    project, projects = _select_user_project("edit")
    if not project:
        return
    new_title   = input(f"Title [{project['title']}]: ").strip() or project['title']
    new_details = input(f"Details [{project['details']}]: ").strip() or project['details']
    project['target'] = get_valid_float_optional(
        f"Target [{project['target']}]: ",
        default=project['target']
    )
    project.update({
        'title': new_title,
        'details': new_details,
        'target': project['target'],
        'start': project['start'],
        'end': project['end']
    })
    save(PROJECTS_FILE, projects)
    print("Project updated.")

def delete_project():
    project, projects = _select_user_project("delete")
    if not project:
        return
    
    confirm = input(f"Type YES to confirm deletion of '{project['title']}': ").strip().lower()
    if confirm == "yes":
        projects.remove(project)
        save(PROJECTS_FILE, projects)
        print("Project deleted.")
    else:
        print("Deletion cancelled.")