"""
Task Logic

format_tasks
- format task into a json object with id, message, and date.
"""


"""
format task into a json object with id, message, and date.
"""
def format_task(task):
    return {"id": task.get('id'),
            "message": task.get('summary'),
            "date": task.get('start', {}).get('date'),  # or just use todays date
            }
