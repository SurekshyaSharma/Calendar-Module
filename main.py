import calendar
import datetime
import time

#calendar
print(calendar.weekheader(3))

print ("-" * 25)
print(calendar.firstweekday())

print ("-" * 25)
print(calendar.month(2020,1))

print ("-" * 25)
print(calendar.monthcalendar(2020,1))

print ("-" * 25)
print (calendar.calendar(2020))

print ("-" * 25)
day_of_the_week = calendar.weekday(2020,1,8)
print(day_of_the_week)

print ("-" * 25)
check_leap = calendar.isleap(2020)
print(check_leap)
leap_days = calendar.leapdays(2020,2040)
print(leap_days)
print ("-" * 25)

#datetime
today = datetime.datetime.now()
print("Today's Date: " + str(today))
print ("Today's Year: " + str (today.year))
print("Today's Month: " + str(today.month))
print("Today's Day: " + str (today.day))
print("Today's Hour: " + str(today.hour))
print("Today's Minute: "  +str(today.minute))
print("Today's Seconds: " + str(today.second))
print ("-" * 25)
print("Week ago: "+ str(today - datetime.timedelta(weeks=1)))
print("100 Days ago: " + str(today - datetime.timedelta(days=100)))
print("Week after today: " + str(today + datetime.timedelta(weeks=1)))
print("100 Days after today: " + str(today + datetime.timedelta(days=100)))
print ("-" * 25)
my_birthday = datetime.datetime(2020,6,11)
print("Birthday in " + str(my_birthday - today))