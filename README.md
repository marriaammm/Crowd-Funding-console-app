# Crowd-Funding-console-app

A simple console-based crowdfunding application that allows users to create and manage fundraising projects.

## Features

### Authentication System
- **User Registration** with the following details:
  - First name
  - Last name
  - Email (validated)
  - Password (with confirmation)
  - Mobile phone (validated for Egyptian numbers)
- **Login/Logout** functionality using email and password
- Session management for authenticated users

### Project Management
- **Create Projects** with:
  - Title
  - Detailed description
  - Funding target amount
  - Start and end dates (with validation)
- **View Projects** 
  - List all available projects
  - See project details including owner, target amount, and duration

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Navigate to the project directory:
```bash
cd crowdfunding-console-app
```

3. No additional dependencies required - uses Python standard library only.

## Usage

1. Run the main application:
```bash
python main.py
```

2. Follow the interactive menu:
- Option 1: Register new user
- Option 2: Login
- Option 3: Create new project (authenticated users only)
- Option 4: List all projects
- Option 5: Logout (authenticated users only)
- Option 0: Exit

## Project Structure

```
crowdfunding-console-app/
├── main.py              # Application entry point
├── auth.py             # Authentication functionality
├── projects.py         # Project management
├── validations.py      # Input validation utilities
├── authValidations.py  # Authentication-specific validations
├── dependencies.py     # File handling and data management
├── data/              # Data storage directory
│   ├── user.json     # User data
│   ├── projects.json # Project data
│   └── session.json  # Current session data
└── .gitignore        # Git ignore configuration
```

## Data Storage
- All data is stored locally in JSON files
- User data, project information, and session details are persisted between runs

## Validation Rules
- Email must follow standard email format
- Phone numbers must be valid Egyptian mobile numbers
- Dates must follow YYYY-MM-DD format
- Project end date must be after start date
- All monetary values must be valid numbers

## Future Improvements
- Project editing functionality
- Project deletion
- Search projects by date
- User profile management
- Project categories
- Funding contribution system

## Similar Projects
- [GoFundMe](https://www.gofundme.com)
- [Kickstarter](https://www.kickstarter.com)
- [Crowdfunding.com](https://www.crowdfunding.com)
