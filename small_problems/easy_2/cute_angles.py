'''
P: input float point angle 0 to 360 inclusive
    output string angle in degrees, minutes, seconds
E: 30 -> '30'00'00"  first ' is degree symbol
D: none
A:
    1. degrees is integer part of input
    2. minute. is integer part of 60 times decimal part of degrees
    3. second is integer part of 60 times decimal part of minutes
    4. put together in f string, guarantee two digits for minutes and secs

for extra credit:
    before step 1 apply mod = 360 to float_degrees

C: below
'''

DEGREE = "\u00B0"
MINUTES_PER_DEGREE = 60
SECONDS_PER_MINUTE = 60

def dms(float_degrees):
    float_degrees %= 360
    int_degrees = int(float_degrees)
    float_minutes = MINUTES_PER_DEGREE * (float_degrees - int_degrees)
    int_minutes = int(float_minutes)
    float_seconds = SECONDS_PER_MINUTE * (float_minutes - int_minutes)
    int_seconds = int(float_seconds)

    return f'''{int_degrees}{DEGREE}{int_minutes:02d}'{int_seconds:02d}"'''

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"