'''
P: input string first and last name, output string last, first name
E: 'Joe Roberts' -> 'Roberts, Joe'
D: none
A: join with ', ' reversed split

    extra credit: concat last, ', ', and join of all other with space
C: below
'''

def swap_name(name_string):
    return ', '.join(name_string.split()[::-1])

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

print()

def swap_name(name_string):
    names_list = name_string.split()
    return names_list[-1] + ', ' + ' '.join(names_list[:-1])

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
