from datetime import timedelta
from datetime import datetime

today = datetime.now()

fdays =today - timedelta(days=5)
print('5 days ago:',fdays)