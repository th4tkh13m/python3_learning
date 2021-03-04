"""
Created on Sun Dec 20 15:46:04 2020

@author: Admin
"""

'''Tic Tac Toe Game'''
# Drawing the board function.             
def boardgame(game_list):
    count_row = 0
    count_collumn = 0
    count_game_list = 0
    while count_row <13:
        while count_collumn < 16:
            if count_row in [0,4,8,12]:
                if count_collumn in board_blank:
                    count_collumn += 1
                    print(' ',end ='')
                    continue
                print('_',end ='')
            else:
                if count_collumn in board_blank:
                    print('|',end ='')
                elif count_row in [2,6,10] and count_collumn in [3,8,13]:
                    print(game_list[count_game_list],end ='')
                    count_game_list += 1
                else:
                    count_collumn += 1
                    print(' ',end ='')
                    continue
            count_collumn += 1
        count_collumn = 0
        print('')
        count_row += 1
# Check what turn and what player will play that turn.
def check_player_turn(turn_count):
    if turn_count % 2 != 0:
        return first_player_choice
    else:
        return second_player_choice
# Change player's desired square value into that player's symbol.
def user_input(game_list):
    position = input('Choose your desired position (1 to 9):')
    while position.isdigit() == False or int(position) not in range(1,10):
        position = input('Please re-enter a valid value (1-9):')
    while game_list[int(position)-1] in acceptable_choice:
        position = input('That square is used. Please choose an unused one.')
    game_list[int(position)-1] = check_player_turn(turn_count)
# Check if the board is full
def check_board(game_list):
    for x in winning_list:
        if len(set([game_list[y] for y in x ])) == 1:
            return True
    for x in game_list:
        if x not in acceptable_choice:
            return False
    return True
# Players enter their info
def player_info():
    global first_player_point, second_player_point, win_point
    first_player_point = 0
    win_point = ''
    second_player_point = 0
    global first_player_choice, second_player_choice, first_player, second_player
    #Player name
    first_player = input('Please enter Player 1 name:')
    second_player = input('Please enter Player 2 name:')
    # Symbol choices for 2 player.
    first_player_choice = input(f'Choose your symbol {acceptable_choice}:')
    while first_player_choice.upper() not in acceptable_choice:
       first_player_choice = input('Please choose again.')
    first_player_choice == first_player_choice.upper()
    if first_player_choice.upper() == 'O':
        second_player_choice = 'X'   
    else: 
        second_player_choice = 'O'
def current_point():
    global first_player_point, second_player_point
    print('Current point:')
    print(f"{first_player}'s point is {first_player_point}")
    print(f"{second_player}'s point is {second_player_point}")
    if first_player_point > second_player_point:
        print(f'{first_player} is winning')
    elif first_player_point == second_player_point:
        print('Draw')
    else:   print(f'{second_player} is winning')
    print(10*'_')
def replay():
        replay_game = input('Do you want to play again? [Y/N]')
        while replay_game.upper() not in ['Y','N']:
            replay_game = input('Please enter a valid answer. Try again.')
        if replay_game.upper() == 'N': return False
def reset_info(win_point):
    reset_point = input('Do you want to reset point and info?')
    while reset_point.upper() not in ['Y','N']:
        reset_point = input('Please enter a valid answer. Try again.')
    if reset_point.upper() == 'Y':
        player_info() 
def game_result(game_list):
    global first_player_point, second_player_point
    for x in winning_list:
        if len(set([game_list[y] for y in x ])) == 1:
            if win_point == first_player_choice:
                first_player_point += 1
            elif win_point == second_player_choice:
                second_player_point += 1
            return first_player if (turn_count-1) % 2 != 0 else second_player
    return False
import os
def clear(): 
    os.system('cls')
board_blank = [0,5,10,15]
game_list = [x for x in range(1,10)]
acceptable_choice = ['O','X']
winning_list = [[0,1,2],[0,3,6],[3,4,5],[6,7,8],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]  
win_point = ''
round_count = 1
player_info()
first_player_point = 0
second_player_point = 0
while True:
    win_point = ''
    turn_count = 1
    while check_board(game_list) == False:
        clear()
        print(f'This is round {round_count}')
        current_point()
        print(f'This is turn {turn_count}')
        boardgame(game_list)
        check_board(game_list)
        check_player_turn(turn_count)
        print(f"Player {(first_player if turn_count %2 != 0 else second_player)}'s turn" )
        user_input(game_list)
        turn_count+=1
    clear()
    boardgame(game_list)
    round_count += 1
    if game_result(game_list) != False:
        win_point = check_player_turn(turn_count-1)
        print(f'Player {game_result(game_list)} win')
    else:
        print('Draw')
    game_list = [x for x in range(1,10)]
    if replay() == False:
        break
    reset_info(win_point)
    
        
        
    
    
    
 
    
        
    
    
    
                    
                    
                    
            
            
    
