"""
get_tomorrows_date
- return tomorrow's date as 'YYYY-MM-DD' string
"""

import datetime

"""
return tomorrow's date as 'YYYY-MM-DD' string
"""
def get_tomorrows_date():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return tomorrow.isoformat()