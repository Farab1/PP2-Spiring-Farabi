from datetime import timedelta
from datetime import datetime

my =  input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
your = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")

mydate = datetime.strptime(my,"%Y-%m-%d %H:%M:%S")
yourdate = datetime.strptime(your,"%Y-%m-%d %H:%M:%S")

diffrence = abs(mydate-yourdate)

secdiff = diffrence.total_seconds()
print('Diffrence in days with seconds:',secdiff)