'''
P:
    input positive int minutes after midnight or negative int minutes
    before midnight
    output string of clock time hh:mm, 24 hour format
E: 0 -> '00:00'
D: none
A: 
    1. convert input minutes to minute of day by modulo 24 * 60
    2. hour = minute // 60, minute = minute % 60, in helper
        function

    extra credit:
    1. make a datetime object with midnight between Saturday and Sunday
        need a base date, use Jan 5, 205
    2. increment of by deltatime object of delta_minutes
    3. output string of day and clocktime
C: below
'''

MIN_PER_HR = 60
HR_PER_DAY = 24

def time_of_day(minutes_past_midnight):

    minute_of_day = minutes_past_midnight % (MIN_PER_HR * HR_PER_DAY)

    return clock_string(minute_of_day)

def clock_string(minutes):
    return f'{minutes // MIN_PER_HR:02d}:{minutes % MIN_PER_HR:02d}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

print()

import datetime as dt

BASE_YEAR = 2025
BASE_MONTH = 1
BASE_DAY = 5

def day_and_time_of_day(delta_minutes):
    base_datetime = dt.datetime(
        year=BASE_YEAR,
        month=BASE_MONTH,
        day=BASE_DAY
    )

    new_datetime = base_datetime + dt.timedelta(minutes=delta_minutes)

    return new_datetime.strftime('%A %H:%M')

print(day_and_time_of_day(-4231) == 'Thursday 01:29')