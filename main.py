from src.gamefunctions import *

while True:
    # Setting up the game
    the_board = [' '] * 10

    player1_marker, player2_marker = player_marker() 
    choose_turn = choose_player()
    print(f"{choose_turn} will play first!")

    game_on = input("Are you ready to play the game (Y or N)? ")

    if game_on.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        break
        
    while game_on:
        if choose_turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print(f"Congradulations! {choose_turn} won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Game Tie!")
                    break
                else:
                    choose_turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print(f"Congradulations! {choose_turn} won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Game Tie!')
                    break
                else:
                    choose_turn = 'Player 1'
                    
    if not replay():
        break