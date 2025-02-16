from datetime import timedelta
from datetime import datetime


today = datetime.now()
print('Today:',today)

tomorrow = datetime.now() + timedelta(days=1)
print('Tomorrow:',tomorrow)

yesterday = datetime.now() + timedelta(days = -1)
print('Yesterday:',yesterday)