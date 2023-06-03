"""
This script is run daily, at the end of the day.

It moves all tasks for the day (that have not been deleted) to tomorrow.
"""

# load env
from dotenv import load_dotenv
load_dotenv()

# load classes
from to_do import push_unfinished_to_do_tasks

if __name__ == '__main__':
    push_unfinished_to_do_tasks()