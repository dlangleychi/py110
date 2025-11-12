'''
P: give two lists with all comparable elements, 
    return one merged sorted list
E: [1, 3], [2, 4] -> [1, 2, 3, 4]
D: new output list
A: if list1 element is greater switch everything, append list1 to ans
    increment pointer, once one list is finished copy rest of the other
C: below
'''

def merge(list1, list2):
    if not list1:
        return list2[:]
    if not list2:
        return list1[:]
    
    n1, n2 = len(list1), len(list2)
    i, j = 0, 0

    merged_list = []

    while i < n1 and j < n2:
        if list1[i] > list2[j]:
            list1, list2 = list2, list1
            n1, n2 = n2, n1
            i, j = j, i
        merged_list.append(list1[i])
        i += 1
    while j < n2:
        merged_list.append(list2[j])
        j += 1

    return merged_list

def merge(list1, list2):
    copy1, copy2 = list1[:], list2[:]

    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)