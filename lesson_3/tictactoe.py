import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_PER_MATCH = 5
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
DEFAULT_SQUARE = 5
PLAYER_MOVES_FIRST = 'choose'
YES_ANSWERS = ['yes', 'y']
NO_ANSWERS = ['no', 'n']

def prompt(message):
    print(f'==> {message}')

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key 
            for key, value in board.items() if 
            value == INITIAL_MARKER]

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt('Sorry, that\'s not a valid choice.')

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if board_full(board):
        return
    
    square = computer_minimax_choice(board)
    board[square] = COMPUTER_MARKER

def make_tuple(board):
    return tuple((square, board[square]) for square in range(1, 10))

minimax_memo = {}
def minimax(board, current_player):
    tuple_board = make_tuple(board)
    if (tuple_board, current_player) in minimax_memo:
        return minimax_memo[(tuple_board, current_player)]
    
    if detect_winner(board) == 'Player':
        ans = 1
    elif detect_winner(board) == 'Computer':
        ans = -1
    elif board_full(board):
        ans = 0
    elif current_player == 'player':
        value = -1
        for square in empty_squares(board):
            new_board = board.copy()
            new_board[square] = HUMAN_MARKER
            value = max(value, 
                minimax(new_board.copy(), alternate_player(current_player)))
        ans = value
    elif current_player == 'computer':
        value = 1
        for square in empty_squares(board):
            new_board = board.copy()
            new_board[square] = COMPUTER_MARKER
            value = min(value, 
                minimax(new_board.copy(), alternate_player(current_player)))
        ans = value

    minimax_memo[(tuple_board, current_player)] = ans
    return ans

def computer_minimax_choice(board):
    square_to_value = {}
    for square in empty_squares(board):
        new_board = board.copy()
        new_board[square] = COMPUTER_MARKER
        square_to_value[square] = minimax(new_board.copy(), 'player')

    return min(square_to_value, key=square_to_value.get)

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (
            board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER
        ):
            return 'Player'
        elif (
            board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER
        ):
            return 'Computer'
        
    return None

def join_or(items_list, delimiter=', ', joining_word='or'):
    match len(items_list):
        case 0:
            return ''
        case 1:
            return str(items_list[0])
        case 2:
            return f'{items_list[0]} {joining_word} {items_list[1]}'
        case _:
            return delimiter.join(map(str, items_list[:-1])) + \
                f'{delimiter}{joining_word} {items_list[-1]}'

def find_at_risk_square(board, marker):
    for line in WINNING_LINES:
        markers = [board[square] for square in line]

        if (markers.count(marker) == 2 
            and markers.count(INITIAL_MARKER) == 1):
            for square in line:
                if board[square] == INITIAL_MARKER:
                    return square
    return None

def choose_square(board, current_player):
    if current_player == 'player':
        player_chooses_square(board)
    elif current_player == 'computer':
        computer_chooses_square(board)

def alternate_player(current_player):
    if current_player == 'player':
        return 'computer'
    elif current_player == 'computer':
        return 'player'

def play_tic_tac_toe():
    while True:
        player_score = 0
        computer_score = 0

        if PLAYER_MOVES_FIRST == 'player':
            starting_player = 'player'
        elif PLAYER_MOVES_FIRST == 'computer':
            starting_player = 'computer'

        elif PLAYER_MOVES_FIRST == 'choose':
            while True:
                prompt('Who plays first? (player or computer)')
                answer = input()

                if answer == 'player':
                    starting_player = 'player'
                    break
                elif answer == 'computer':
                    starting_player = 'computer'
                    break
                else:
                    prompt("Invalid choice. Please choose again.")

        while True:
            board = initialize_board()
            current_player = starting_player
            while True:
                
                display_board(board)
                choose_square(board, current_player)
                current_player = alternate_player(current_player)
                if someone_won(board) or board_full(board):
                    break

            display_board(board)

            if someone_won(board):
                prompt(f"{detect_winner(board)} won!")
                if detect_winner(board) == 'Player':
                    player_score += 1
                else:
                    computer_score += 1
            else:
                prompt("It's a tie!")

            prompt(f'The match score is; player: {player_score}, computer: {computer_score}')
            input('Press Enter to continue.')

            if player_score > GAMES_PER_MATCH / 2:
                prompt('Player wins the match')
                break
            elif computer_score > GAMES_PER_MATCH / 2:
                prompt('Computer wins the match')
                break

        while True:
            prompt("Play again? (y or n)")
            answer = input().lower()

            if answer in YES_ANSWERS or answer in NO_ANSWERS:
                break
            
            prompt("Invalid response.  Please try again.")

        if answer in NO_ANSWERS:
            break
        
    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()
