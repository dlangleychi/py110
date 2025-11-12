'''
P: given a list, return a new sorted list using merge sort
    with partitioning and merging
E: [3, 1, 2] -> [1, 2, 3]
D: new output list
A: apply partition and then merge_list
    partition: if list has one element return list,
        else return list of two sublists
    merge_list: if list elements are lists, merge them,
        else call merge from before
C:
'''

def partition(ls):
    if len(ls) <= 1:
        return ls
    
    n = len(ls)
    return [partition(ls[:n//2]), partition(ls[n//2:])]

print(partition([9, 2, 7, 6, 8, 5, 0, 1])) 

def merge_list(ls):
    ls1, ls2 = ls[0], ls[1]

    if ls1 and isinstance(ls1[0], list):
        ls1 = merge_list(ls1)

    if ls2 and isinstance(ls2[0], list):
        ls2 = merge_list(ls2)

    return merge(ls1, ls2)

def merge(list1, list2):
    copy1, copy2 = list1[:], list2[:]

    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2

print(merge_list([[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]] ))

def merge_sort(ls):
    return merge_list(partition(ls))

def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    
    ls1 = merge_sort(ls[:len(ls)//2])
    ls2 = merge_sort(ls[len(ls)//2:])

    return merge(ls1, ls2)

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)