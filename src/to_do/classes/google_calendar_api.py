"""
CRUD for storing strings on google calendar

get_tasks_for_day
-

create_task
-

update_task
-

delete_task
-

move_task_to_date
- move a task from today to a specified date

move_unfinished_tasks_to_tomorrow
- move all remaining tasks from today to tomorrow
"""

from __future__ import print_function

import datetime
import os.path
import os
import re

from util.date import get_tomorrows_date
from util.get_ip import get_ip

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleCalenderAPI:

    SCOPES = ['https://www.googleapis.com/auth/calendar']
    CREDS = None
    CALENDAR_ID = os.environ['CALENDAR_ID']


    def __init__(self):
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            self.CREDS = Credentials.from_authorized_user_file(
                'token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.CREDS or not self.CREDS.valid:
            if self.CREDS and self.CREDS.expired and self.CREDS.refresh_token:
                try:
                    self.CREDS.refresh(Request())
                except RefreshError as e:
                    self.CREDS = None
                    os.remove('token.json')
                    return self.__init__()
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'google-calendar-secret.json', self.SCOPES)
                # Me stuff
                # this is running on a raspberry pi which uses a random
                # ip on the local network.
                # gotta get the ip and use it as the return address
                # pi_ip = get_ip()
                self.CREDS = flow.run_local_server(
                    open_browser=False, port=5001)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.CREDS.to_json())


    #
    def get_tasks_for_day(self):
        try:
            service = build('calendar', 'v3', credentials=self.CREDS)

            # calendar_list = service.calendarList().list().execute()
            # [print(cal) for cal in calendar_list.get('items')]

            # Call the Calendar API
            now = datetime.datetime.today()
            start_of_today = datetime.datetime(
                now.year, now.month, now.day, 0, 0, 0)
            start_of_today = start_of_today.isoformat() + 'Z'
            events_result = service.events().list(calendarId=self.CALENDAR_ID, timeMin=start_of_today,
                                                  maxResults=50, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])

            # sort tasks by index
            # events.sort(key = lambda event: event.get('summary'))
            return events

        except HttpError as error:
            print('An error occurred: %s' % error)
            # log this error
            return []


    #
    def create_task(self, text, date):
        try:
            service = build('calendar', 'v3', credentials=self.CREDS)

            # Call the Calendar API
            event = {'summary': text, 'start': {'date': date}, 'end': {'date': date}}
            event = service.events().insert(
                calendarId=self.CALENDAR_ID, body=event).execute()

            return event

        except HttpError as error:
            print('An error occurred: %s' % error)
            # log this error
            return []


    #
    def delete_task(self, task_id):
        try:
            service = build('calendar', 'v3', credentials=self.CREDS)

            # Call the Calendar API
            event = service.events().delete(
                calendarId=self.CALENDAR_ID, eventId=task_id).execute()
            return event

        except HttpError as error:
            print('An error occurred: %s' % error)
            # log this error
            return []


    # Move a task from today to a specified date
    def move_task_to_date(self, task_id, date):
        try:
            service = build('calendar', 'v3', credentials=self.CREDS)

            # Call the Calendar API
            update = {'start': {'date': date}, 'end': {'date': date}}
            event = service.events().patch(
                calendarId=self.CALENDAR_ID, eventId=task_id, body=update).execute()
            return event

        except HttpError as error:
            print('An error occurred: %s' % error)
            # log this error
            return []


    #
    def move_unfinished_tasks_to_tomorrow(self):
        # get all tasks for today
        tasks = self.get_tasks_for_day()
        tomorrow = get_tomorrows_date()

        for task in tasks:
            task_id = task.get('id')
            self.move_task_to_date(task_id, tomorrow)

        return True