'''
P: take a positive integer input, return True if prime, False otherwise
E: 1 -> False
D: none
A: loop through integers > 1 with square less than input, 
    if any divide return False, otherwise True
C: below 
'''

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i**2 <= num:
        if num % i == 0:
            return False
        i += 1
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True

