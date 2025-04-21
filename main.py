from auth import register, login, logout, get_current_user
from projects import create_project, list_projects, edit_project, delete_project

def main():
    while True:
        user = get_current_user()
        print("\n--- Crowdfunding App ---")
        
        if user:
            print("3. Create Project")
            print("4. List Projects")
            print("5. Edit Project")
            print("6. Delete Project")
            print("7. Logout")  
        else:
            print("1. Register")
            print("2. Login")
            print("4. List Projects")  

        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1" and not user:  
            register()
        elif choice == "2" and not user:  
            login()
        elif choice == "3" and user: 
            create_project()
        elif choice == "4":
            list_projects()
        elif choice == "5" and user:  
            edit_project()
        elif choice == "6" and user:
            delete_project()
        elif choice == "7" and user:
            logout()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
