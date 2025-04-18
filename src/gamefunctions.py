# from IPython.display import clear_output
import random

# Display the Tic Tac Toe board
def display_board(board):
    print(' ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + ' ')
    print('--- | --- | ---')
    print(' ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + ' ')
    print('--- | --- | ---')
    print(' ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + ' ')
    
# Player choose a marker either 'X' or 'O'
def player_marker():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Please select your marker 'X' or 'O': ").upper()
        
        if marker not in ('X', 'O'):
            print("Incorrect input, pick 'X' or 'O'!")
            
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Place the player's marker at choosen position
def place_marker(board, marker, position):
    board[position] = marker

# Check to see of the picked position is free, if free return TRUE, if taken return FALSE
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

# Player choose the position where they want to place the marker, return the picked position
def player_choice(board):
    position_choice = 0
    
    while position_choice not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position_choice):
        position_choice = int(input("Please pick a number between (1-9) to place your marker: "))
        
        if position_choice not in [1,2,3,4,5,6,7,8,9]:
            print('Wrong input, the board only accepts (1-9). [7-9] => top row, [4-6] => middle row, [1-3] => bottom row.')
        elif not space_check(board, position_choice):
            print('That position is taken, please pick another position.')
            
    return position_choice
    
# Check win if there are three of the same markers in a row
def win_check(board,marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # Checks top row
            (board[4] == marker and board[5] == marker and board[6] == marker) or # Checks mid row
            (board[1] == marker and board[2] == marker and board[3] == marker) or # Checks bottom row
            (board[1] == marker and board[5] == marker and board[9] == marker) or # Checks diagonal starting from bottom left corner to top right corner
            (board[3] == marker and board[5] == marker and board[7] == marker) or # Checks diagnoal starting from bottom right corner to top left corner
            (board[7] == marker and board[4] == marker and board[1] == marker) or # Checks left column
            (board[8] == marker and board[5] == marker and board[1] == marker) or # Checks mid column
            (board[9] == marker and board[6] == marker and board[3] == marker)) # Checks right column

# Check if the board is full, return TRUE if board is full, return FALSE if board is not full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Choose who goes first with randomization
def choose_player():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

# Asks if the player wants to play again
def replay():
    return input("Do you want to play again (Y or N)? ").lower().startswith('y')


