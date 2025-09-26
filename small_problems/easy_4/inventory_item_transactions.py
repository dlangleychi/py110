'''
P: input int item ID, list of dictionaries representing transactions
    output return new (assumed) list of transaction for the specific
    item
E: 101, [{'id': 101}, {id': 102}] -> [{'id': 101}]
D: list created for output
A: list comprehension iterate of transactions filter for desired id
C: below
'''

def transactions_for(desired_id, transaction_list):
    return [
        transaction
        for transaction in transaction_list
        if transaction['id'] == desired_id
    ]

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True