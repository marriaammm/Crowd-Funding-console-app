from datetime import datetime
import re

DATE_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def get_valid_float(prompt: str) -> float:
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid amount. Please enter a number.")

def get_valid_date(prompt: str, start_date: datetime = None) -> datetime:
    while True:
        date_str = input(prompt).strip()
        if not DATE_REGEX.match(date_str):
            print("Invalid date format. Try again (YYYY-MM-DD).")
            continue
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            if start_date and date <= start_date:
                print("End date must be after start date. Try again.")
                continue
            return date
        except ValueError:
            print("Invalid date value. Please enter a valid date.")
