from datetime import datetime

dt = datetime.now()

formatted = dt.strftime("%d.%m.%Y %H:%M")
print('time without microsec:',formatted)