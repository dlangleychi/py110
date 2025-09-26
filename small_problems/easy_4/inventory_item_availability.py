'''
P: input int item id, transaction list
    output True of False on whether the total quantity present is
    greater than zero, 'movement': 'in' -> increased quantity,
    'out' -> decreased quantity
E: 101, [{'id': 101, 'movmement': 'out', 'quantity': 1}] -> False
D: list comprehensions for totaling ins and outs
A: iterate through transaction_for increment inventory for 'in',
    decrement for 'out', return inventory > 0
C: below
'''

def transactions_for(desired_id, transaction_list):
    return [
        transaction
        for transaction in transaction_list
        if transaction['id'] == desired_id
    ]

def is_item_available(item_id, transaction_list):
    item_inventory = 0

    for transaction in transactions_for(item_id, transaction_list):
        if transaction['movement'] == 'in':
            item_inventory += transaction['quantity']
        elif transaction['movement'] == 'out':
            item_inventory -= transaction['quantity']

    return item_inventory > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True