from datetime import datetime
from auth import get_current_user
from dependancies import load, save, PROJECTS_FILE
from validations import get_valid_float, get_valid_date  

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