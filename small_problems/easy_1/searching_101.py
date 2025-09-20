'''
P: take six int inputs, print whether # six appears in first five
E: 25,15,20,17,23,17 -> yes it appears
D: none
A: put inputs into list, check if last appears in first five
C: below
'''

ORDINALS = [
    '1st', '2nd', '3rd', '4th', '5th', 'last'
]

number_list = [None] * 6

for i in range(6):
    number_list[i] = int(input(f'Enter the {ORDINALS[i]} number: '))

if number_list[-1] in number_list[:-1]:
    print(f'\n{number_list[-1]} is in '
          f'{','.join(map(str, number_list[:-1]))}')
else:
    print(f'\n{number_list[-1]} isn\'t in '
          f'{','.join(map(str, number_list[:-1]))}')
