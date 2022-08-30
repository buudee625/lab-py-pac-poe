game_over = False
row1 = ['','','']
row2 = ['','','']
row3 = ['','','']

def game_engine():
    print('----------------------\nLet\'s play Py-Pac-Poe!\n----------------------')
    show_board()
    while True:
        o_turn()
        show_board()
        referee()
        if game_over:
            break
        x_turn()
        show_board()
        referee()
        if game_over:
            break
    # play_again = input('Play again? (Enter \'Y\' to duel again!)').lower()
    # if play_again == 'y':
    #     game_engine()
    # else:
    #     print('Thanks for playing! Have a joyous day!')

def show_board():  
    print(row1)
    print(row2)
    print(row3)

def o_turn():
    while True:
        o_turn = input('Player O\'s move (example B2): ').lower()
        if o_turn == 'a1' and not row1[0]:
            row1[0] = 'O'
            break
        elif o_turn == 'a2' and not row2[0]:
            row2[0] = 'O'
            break
        elif o_turn == 'a3' and not row3[0]:
            row3[0] = 'O'
            break
        elif o_turn == 'b1' and not row1[1]:
            row1[1] = 'O'
            break
        elif o_turn == 'b2' and not row2[1]:
            row2[1] = 'O'
            break
        elif o_turn == 'b3' and not row3[1]:
            row3[1] = 'O'
            break
        elif o_turn == 'c1' and not row1[2]:
            row1[2] = 'O'
            break
        elif o_turn == 'c2' and not row2[2]:
            row2[2] = 'O'
            break
        elif o_turn == 'c3' and not row3[2]:
            row3[2] = 'O'
            break
        else:
            print('Bogus move! Try again...')
            continue

def x_turn():
    while True:
        x_turn = input('Player X\'s move (example B2): ').lower()
        if x_turn == 'a1' and not row1[0]:
            row1[0] = 'X'
            show_board()
            break
        elif x_turn == 'a2' and not row2[0]:
            row2[0] = 'X'
            show_board()
            break
        elif x_turn == 'a3' and not row3[0]:
            row3[0] = 'X'
            show_board()
            break
        elif x_turn == 'b1' and not row1[1]:
            row1[1] = 'X'
            show_board()
            break
        elif x_turn == 'b2' and not row2[1]:
            row2[1] = 'X'
            show_board()
            break
        elif x_turn == 'b3' and not row3[1]:
            row3[1] = 'X'
            show_board()
            break
        elif x_turn == 'c1' and not row1[2]:
            row1[2] = 'X'
            show_board()
            break
        elif x_turn == 'c2' and not row2[2]:
            row2[2] = 'X'
            show_board()
            break
        elif x_turn == 'c3' and not row3[2]:
            row3[2] = 'X'
            show_board()
            break
        else:
            print('Bogus move! Try again...')
            continue

def referee():
    global game_over
    # check horizontal winning
    if '' not in row1 or '' not in row2 or '' not in row3: 
        if len(set(row1)) == 1 or len(set(row2)) == 1 or len(set(row3)) == 1:
            if 'O' in set(row1[0]) or 'O' in set(row2[0]) or 'O' in set(row3[0]):
                print('O won horizontal')                
                game_over = True
            else:
                print('X won horizontal')
                game_over = True
    # check vertical winning
    # if row1[0] != '' and row1[1] != '' and row1[2] != '':
    #     if row1[0] == row2[0] == row3[0] or row1[1] == row2[1] == row3[1] or row1[2] == row2[2] == row3[2]:
    #         if 'O' in row1[0] or 'O' in row1[1] or 'O' in row1[2]:
    #             print('O won vertical')                
    #             game_over = True
    #         else: 
    #             print('X won vertical')
    #             game_over = True
    # check diagonal winning
    if '' not in row2[1]:
        if row1[0] == row2[1] == row3[2] or row1[2] == row2[1] == row3[0]:
            if 'O' in row2[1]:
                print('O won diagonal')                
                game_over = True
            else: 
                print('X won diagonal')
                game_over = True
                
game_engine()
# print('Player O emerges victorious in this fearsome battle!') 


# def display_game(icon):
#     unicode = 65

#     # First row
#     print(f'  ', end='')
#     for i in range(3):
#         print(f'  {chr(unicode + i)} ', end='')
#     print('\n')

#     # Other rows
#     for x in range(3):
#         print(f'{x + i} ', end='')
#         for i in range(3):
#             print(f'  {icon} ', end='')
#         print("| ")
#         print((3*4+4)*"-")




