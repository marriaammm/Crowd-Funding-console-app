# Crowd‑Funding Console App

A simple console‑based crowdfunding application that allows users to register, log in, and manage fundraising projects using local JSON files for storage.

## Features

### Authentication
- **Register** new users (auto‑logs in upon success)  
  - First name  
  - Last name  
  - Email (validated with regex)  
  - Password (with confirmation)  
  - Mobile phone (Egyptian format, validated)  
- **Login** by email + password  
- **Logout** clears your session  
- Session persists across runs via `data/session.json`

### Project Management
- **Create** a new project  
  - Title, description, target amount, start/end dates (validated)  
- **Edit My Project** (only your own)  
- **Delete My Project** (only your own)  
- **Search Projects by Date** (find campaigns active on a given day)  
- **List All Projects** (publicly available)

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/marriaammm/Crowd-Funding-console-app.git
   ```
2. Enter the project directory:  
   ```bash
   cd Crowd-Funding-console-app
   ```
3. (Optional) Create a virtual environment and activate it:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```
4. No external dependencies—everything uses Python’s standard library.

## Usage

Run the application:

```bash
python main.py
```

You’ll see a menu that adapts based on your login state:

```
--- Crowdfunding App ---
1. Register
2. Login
7. List All Projects
0. Exit
```

After registering or logging in, the menu becomes:

```
--- Crowdfunding App ---
3. Create Project
4. Edit My Project
5. Delete My Project
6. Search Projects by Date
7. List All Projects
8. Logout
0. Exit
```

Just enter the number of the action you want.

## Project Structure

```
Crowd‑Funding-console-app/
├── main.py               # Entry point & interactive menu
├── auth.py               # Register, login, logout, session logic
├── authValidations.py    # Email & phone validation helpers for auth
├── projects.py           # Create, edit, delete, search, list projects
├── validations.py        # Numeric & date‑format helpers
├── dependancies.py       # JSON load/save, file paths, regex constants
├── data/                 # JSON storage (auto‑created)
│   ├── user.json         # Registered users
│   ├── projects.json     # Project records
│   └── session.json      # Current user session
└── .gitignore            # Files/folders to ignore in Git
```

## Validation Rules

- **Email** must match standard pattern (e.g. `user@example.com`)  
- **Phone** must match Egyptian mobile format: `010/011/012/015 + 8 digits`  
- **Dates** must be `YYYY‑MM‑DD` and end > start  
- **Amounts** must be numeric (floats allowed)

## .gitignore

Make sure you have a `.gitignore` with entries like:

```
__pycache__/
*.pyc

data/user.json
data/projects.json
data/session.json

venv/
```

This prevents committing user data, sessions, or cache.

Enjoy building and extending your console crowdfunding app!
