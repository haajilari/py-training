import sys

locations = sys.path
print(locations)
for i in locations:
    print(i)


import calendar

leap_days = calendar.leapdays(2000, 2090)
print(leap_days)
is_it_leap = calendar.isleap(2024)

print(is_it_leap)