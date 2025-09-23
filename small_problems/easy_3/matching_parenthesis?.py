'''
P: input string, output boolean if string is balanced
E: 'What (is) this?' -> True
D: none
A: keep a tally of open parenthesis,
    loop through string increment on open
    decrement on close, if negative, return False
    return opens equal zero

    extra credit: maintain stack of required closings
    if char is close
        if stk and if char == stk[-1]
            stk pop
        else if char is open
            stk append open to close [char]
        return False
    if char is open
        stk append open to close [char]

    return not stk

C: below
'''

'''
def is_balanced(string):
    open_parenthesis = 0
    
    for char in string:
        if char == '(':
            open_parenthesis += 1
        elif char == ')':
            open_parenthesis -= 1
            if open_parenthesis < 0:
                return False
    
    return open_parenthesis == 0
'''

OPEN_TO_CLOSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '\"': '\"',
    '\'': '\''
}

CLOSES = OPEN_TO_CLOSE.values()

def is_balanced(string):
    closes_owed = []

    for char in string:
        if char in CLOSES:
            if closes_owed and closes_owed[-1] == char:
                closes_owed.pop()
            elif char in OPEN_TO_CLOSE:
                closes_owed.append(OPEN_TO_CLOSE[char])
            else:
                return False
        elif char in OPEN_TO_CLOSE:
            closes_owed.append(OPEN_TO_CLOSE[char])

    return not closes_owed

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

print()

print(is_balanced('"') == False)
print(is_balanced(']]') == False)
print(is_balanced('[]()') == True)
