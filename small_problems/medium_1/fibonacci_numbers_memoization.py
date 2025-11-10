'''
P: calculate nth fibonacci number with recurssion and memoization
E: 1 -> 1
D: memo dictionary
A: if value is in dictionary return existing value, 
    else calculate and store
C: below
'''

fibonacci_memo = {}

def fibonacci(n):
    if n in fibonacci_memo:
        return fibonacci_memo[n]
    
    if n <= 2:
        ans = 1
    else:
        ans = fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci_memo[n] = ans
    return ans

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True