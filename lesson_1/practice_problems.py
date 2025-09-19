
# 1

fruits = ("apple", "banana", "cherry", "date", "banana")

# print(fruits.count('banana'))

# 2

# length is 5

numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers))

# 3

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# print(a|b)
# print(a.union(b))
# print(b.union(a))

# 4

# {'Fred': 0, 'Barney': 1, 'Wilma': 2, 'Betty' : ...
# 3, 'Pebbles' : 4, 'Bambam': 5}

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
# print(name_positions)

# 5

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# print(sum(ages.values()))

# 6

# print(min(ages.values()))

# 7

# ['bear']

words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

# print(selected_words)

# 8

statement = "The Flintstones Rock"

char_to_count = {}

for char in statement:
    if not char.isspace():
        char_to_count[char] = char_to_count.get(char, 0) + 1

# print(char_to_count)

# 9

# [2, 3]

test = [num for num in [1, 2, 3] if num > 1]
# print(test)

# 10

# ('b', 'bear')

dictionary = {'a': 'ant', 'b': 'bear'}
# print(dictionary.popitem())

# 11

# [1, 2]

lst = [1, 2, 3, 4, 5]
# print(lst[:2])

# 12

# Doesn't print anything instead it throws error:
# AttributeError: 'frozenset' object has no attribute 'add'

frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)
# print(frozen)

