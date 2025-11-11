'''
P: given a string, return dictionary of percentages lower, upper,
    and neither
E: 'abCdef 123' -> {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
D: return dictionary
A: loop through string counting lower, upper, return dict of 
    percentages
C: below
'''

def letter_percentages(string):
    lower_count = 0
    upper_count = 0
    length = len(string)

    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1

    return {
        'lowercase': f'{100 * lower_count/length:.2f}',
        'uppercase': f'{100 * upper_count/length:.2f}',
        'neither': f'{100 * (length - lower_count - upper_count)/length:.2f}',
    }

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)