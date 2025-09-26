'''
P: input string
    output all nonempty substrings order by starting index, length
E: 'abc' -> ['a', 'ab', 'abc', 'b', 'bc', 'c']
D: list for output
A: iterate through starting positions, each time concatenate 
    leading_substrings to answer

    alt: list comprehension by iterate over starting index 
    and ending index
C: below
'''

def leading_substrings(string):
    return [string[:end] for end in range(1, len(string) + 1)]

def substrings(string):
    result = []
    
    for start in range(len(string)):
        result.extend(leading_substrings(string[start:]))
    
    return result

def substrings_alt(string):
    return [
        string[start:end] 
        for start in range(len(string)) 
        for end in range(start + 1, len(string) + 1)\
    ]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
print(substrings_alt('abcde') == expected_result)  # True