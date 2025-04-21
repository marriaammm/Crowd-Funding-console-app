import os 
import json

DATA_DIR ="data"
USER_FILE = os.path.join(DATA_DIR, "user.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")
SESSION_FILE = os.path.join(DATA_DIR, "session.json")


def load(path, default=None):
    if default is None:
        default = []
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path, exist_ok=True)
    if not os.path.exists(path):
        save(path, default)  
        return default
    try:
        with open(path, "r") as f:
            content = f.read().strip()
            if not content:
                return default
            return json.loads(content)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {path}. Resetting it.")
        return default


def save(path, data):   
    dir_path = os.path.dirname(path)
    if dir_path:
        os.makedirs(dir_path,exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

