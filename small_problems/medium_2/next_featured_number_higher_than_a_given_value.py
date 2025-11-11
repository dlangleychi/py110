'''
P: given integer, return next featured number, or error if not possible
E: 12 -> 21
D: none
A: top up integer to next oddseven multiple, while true check 
    if conditions are met, increment by 14, each time check for
    exceeding 10 digits
C: below
'''

UPPER_LIMIT = 10 ** 10

ERROR_MSG = ("There is no possible number that "
         "fulfills those requirements.")

def next_featured(num):
    num_mod_14 = num % 14

    if num_mod_14 < 7:
        candidate = num + (7 - num_mod_14)
    else:
        candidate = num + (14 - num_mod_14) + 7

    while candidate < UPPER_LIMIT:
        if len(str(candidate)) == len(set(str(candidate))):
            return candidate
        candidate += 14
        
    return ERROR_MSG

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True