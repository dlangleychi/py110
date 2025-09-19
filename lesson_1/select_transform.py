produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(produce_dict):
    result_dict = {}
    for key, val in produce_dict.items():
        if val == 'Fruit':
            result_dict[key] = val

    return result_dict

# print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

def double_numbers(number_list):
    for i in range(len(number_list)):
        number_list[i] *= 2

my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_numbers(my_numbers)) # None
# print(my_numbers)                 # [2, 8, 6, 14, 4, 12]

def double_odd_indexes(numbers):
    result = []
    for idx, num in enumerate(numbers):
        if idx % 2:
            result.append(num * 2)
        else:
            result.append(num)

    return result

# print(double_odd_indexes(my_numbers)) # [1, 8, 3, 14, 2, 12]

def multiply(numbers, multiplier):
    multiplied_numbers = []
    for num in numbers:
        multiplied_numbers.append(num * multiplier)

    return multiplied_numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]