import datetime
today = datetime.datetime.now()

if today.weekday() == 5 or today.weekday() == 6:
    print("It's weekend!")
elif today.weekday()==0:
    print("Today is Monday!")
else:
    print('Working Day!')


if today.weekday() in [5, 6]:
    print("It's weekend!")
else:
    print('Work!')