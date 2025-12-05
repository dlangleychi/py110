'''
P: given list of integers, determine how much must be added to their sum
    to make the next prime number
E: [5,2] -> 4
D: might need list of primes
A: maintain a list of prime, iterate through natural numbers,
    each number you check if divisible by an already discovered prime,
    if not append to primes, if new prime is greater than sum stop
C: below
'''

def nearest_prime_sum(num_list):
    list_sum = sum(num_list)
    primes = []
    i = 2
    while True:
        for prime in primes:
            if i % prime == 0:
                break
        else:
            if i > list_sum:
                return i - list_sum
            primes.append(i)
        i += 1

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)