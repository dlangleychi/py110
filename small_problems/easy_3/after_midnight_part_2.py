'''
P: input sting clock time, output int number minutes
    before or after midnight
E: after: '12:34' -> 754, before: '12:34' -> 686
D: none
A: after: 60 * hours + minutes, before: 1440 - 60 * hours - minutes
    check before = '00:00' and after = '24:00' by module 1440

    extra_credit:
    make datetime object from clock time
    after: return minutes of input - midnight
    before: return minutes of  midnight - input mod 1440
C: below
'''

MIN_PER_HOUR = 60
HOUR_PER_DAY = 24
MIN_PER_DAY = MIN_PER_HOUR * HOUR_PER_DAY

def after_midnight(string_time):
    hours, minutes = parse_time(string_time)
    return (hours * MIN_PER_HOUR + minutes) % MIN_PER_DAY

def before_midnight(string_time):
    hours, minutes = parse_time(string_time)
    return (MIN_PER_DAY - (hours * MIN_PER_HOUR + minutes)) % MIN_PER_DAY

def parse_time(string_time):
    return [int(unit) for unit in string_time.split(':')]

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

print()

from datetime import datetime, timedelta

SECOND_PER_MIN = 60
MIDNIGHT_STRING = '00:00'

def after_midnight(string_time):
    time_delta = convert_time(string_time) \
        - convert_time(MIDNIGHT_STRING)
    return int(time_delta.total_seconds() // SECOND_PER_MIN)

def before_midnight(string_time):
    time_delta = convert_time(MIDNIGHT_STRING) \
        - convert_time(string_time)
    return int(time_delta.total_seconds() // SECOND_PER_MIN) % MIN_PER_DAY

def convert_time(string_time):
    string_time = string_time.replace('24:00', '00:00')
    return datetime.strptime(string_time, '%H:%M')

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True