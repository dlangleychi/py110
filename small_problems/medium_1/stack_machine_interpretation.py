'''
P: make stack register machine that takes commands as a space
    seperated string
E: 'PRINT' -> 0
D: stack
A: split the string, iterate through commands with match case
    store stack and register values as ints not strings
C: below
'''

def minilang(command_string):
    stack = []
    register = 0
    commands = command_string.split()
    try:
        for command in commands:
            match command:
                case 'PUSH':
                    stack.append(register)
                case 'ADD':
                    register = stack.pop() + register
                case 'SUB':
                    register = register - stack.pop()
                case 'MULT':
                    register = stack.pop() * register
                case 'DIV':
                    register = register//stack.pop()
                case 'REMAINDER':
                    register = register % stack.pop()
                case 'POP':
                    register = stack.pop()
                case 'PRINT':
                    print(register)
                case _:
                    register = int(command)
    except IndexError:
        return 'Sorry, you tried to pop from an empty stack.'
    except ValueError:
        return f'Sorry, invalid token: {command}'
    return None

            

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

print(minilang('POP'))
# empty stack pop error

print(minilang('cat'))
# invalid value error