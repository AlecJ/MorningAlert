"""
The To Do Module handles fetching to do tasks, and moving tasks to different days (if necessary).
Tasks are stored in google calendar as day-long events.

get_to_do_data
- get all tasks for today

push_unfinished_to_do_tasks
- update all tasks for today and set their start/end date to tomorrow.
"""

from .classes.google_calendar_api import GoogleCalenderAPI

client = GoogleCalenderAPI()

# Get all tasks for today
def get_to_do_data():
    data = client.get_tasks_for_day()
    return data or []


# Update all tasks for today and set their start/end date to tomorrow.
def push_unfinished_to_do_tasks():
    client.move_unfinished_tasks_to_tomorrow()
