'''
P: given integer year, return number of Friday 13th in that year
E: 1986 -> 1
D: none
A: using datetime.date object iterate through days of year
    increment counter if day is Friday the 13th
C: below
'''

import datetime

WEEKDAY_FRIDAY = 4

def friday_the_13ths(year):
    friday_the_13th_count = 0
    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == WEEKDAY_FRIDAY:
            friday_the_13th_count += 1
    return friday_the_13th_count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
