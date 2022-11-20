import random

# State variables 
# ====================
game_on = True
player_symbol = ''
player_turn = True 
# True = O, False = X

# Game initialization
# ====================

# Sets up the game and declare global variables
def init():
    global game_on, rowA, rowB, rowC, turn_counter
    turn_counter = 0
    rowA = [' ',' ',' ']
    rowB = [' ',' ',' ']
    rowC = [' ',' ',' ']
    intro()
    while turn_counter < 9 and game_on == True:
        gameboard()
        player_move()
        winning_logic()
        turn_counter += 1
    repeat_game()

# Determine if O or X will go first
def intro():
    print('====================================')
    print("Welcome to Py-Pac-Poe...")
    print('====================================')
    input_num = ''
    while input_num.isdigit() == False:
        input_num = input("Let's see who goes first shall we? Please pick one: 0 or 1? ")
        if input_num.isdigit() == False or int(input_num) not in [0, 1]:
            print("Aren't ya a naughty one! Please pick between 0 or 1!")
            input_num = ''
    if int(input_num) == random.randint(0, 1):
        print("Ara... Player O will go first!")
        turn_switch('o')
    else:
        print("Ara... Player X will go first!")
        turn_switch('x')

# Displays the game board
def gameboard():
    print('\n', 'This is the current game progress:')
    print('==================================', '\n')
    print('  |  1  |  2  |  3  |')
    print('-----------------------')
    print('A | ', rowA[0], ' | ', rowA[1], ' | ', rowA[2], ' |')
    print('-----------------------')
    print('B | ', rowB[0], ' | ', rowB[1], ' | ', rowB[2], ' |')
    print('-----------------------')
    print('C | ', rowC[0], ' | ', rowC[1], ' | ', rowC[2], ' |')
    print('')

# Switches turns betwen O and X  
def turn_switch(p):
    global player_symbol
    global player_turn
    if p.lower() == 'o':
        player_turn = True
        player_symbol = 'O'
    if p.lower() == 'x':
        player_turn = False
        player_symbol = 'X'

# Requests player's input to place the marker and validates the placement, does not concern turn
def player_move():
    while True:
        pos_row = input(f'Player {player_symbol}, please pick a row (A, B or C): ')
        if pos_row.lower() not in ['a', 'b', 'c']:
            print('Ara, you naughty one, you are supposed to only enter A, B or C. Now try again.')
        else:
            print('You picked: ', pos_row)
            break
    while True:
        pos_col = input(f'Player {player_symbol}, please pick a column (1, 2 or 3): ')
        if pos_col.isdigit() == False or int(pos_col) not in [1, 2, 3]:
            print('Ara, you naughty one, you are supposed to only enter 1, 2 or 3. Now try again.')
        else:
            pos_col = int(pos_col)
            print('You picked: ', pos_col)
            validate_move(pos_row, pos_col)
            break

# Check if the position has already been taken, if not, update the board
def validate_move(row, col):
    if row.lower() == 'a':
        if rowA[col - 1] == ' ':
            update_gameboard(row, col)
        else:
            print("Ara, this place is already taken! Let's try again shall we?")
            player_move()
    elif row.lower() == 'b':
        if rowB[col - 1] == ' ':
            update_gameboard(row, col)
        else:
            print("Ara, this place is already taken! Let's try again shall we?")
            player_move()
    elif row.lower() == 'c':
        if rowC[col - 1] == ' ':
            update_gameboard(row, col)
        else:
            print("Ara, this place is already taken! Let's try again shall we?")
            player_move()

# Make changes to the board, updates the gamebaord and switches turn
def update_gameboard(row, col):
    if row.lower() == 'a':
        rowA[col - 1] = player_symbol
    elif row.lower() == 'b':
        rowB[col - 1] = player_symbol
    elif row.lower() == 'c':
        rowC[col - 1] = player_symbol
    gameboard()
    if player_turn == True:
        turn_switch('x')
    else:
        turn_switch('o')
        
# Checks for winning conditions and ending the game
def winning_logic():
    global game_on
    setA = set(rowA)
    setB = set(rowB)
    setC = set(rowC)

    # Horizontal winning conditions
    if len(setA) == 1 and rowA[0] != ' ':
        if rowA[0] == 'O':
            print('Omedetō! Player O secured a victory with a horizontal line in row A <3')
        else:
            print('Omedetō! Player X secured a victory with a horizontal line in row A <3')
        game_on = False
    if len(setB) == 1 and rowB[0] != ' ':
        if rowB[0] == 'O':
            print('Omedetō! Player O secured a victory with a horizontal line in row B <3')
        else:
            print('Omedetō! Player X secured a victory with a horizontal line in row B <3')
        game_on = False
    if len(setC) == 1 and rowC[0] != ' ':
        if rowC[0] == 'O':
            print('Omedetō! Player O secured a victory with a horizontal line in row C <3')
        else:
            print('Omedetō! Player X secured a victory with a horizontal line in row C <3')
        game_on = False

    # Vertical winning conditions
    if (rowA[0] == 'O' and rowB[0] == 'O' and rowC[0] == 'O') or (rowA[0] == 'X' and rowB[0] == 'X' and rowC[0] == 'X'):
        if rowA[0] == 'O':
            print('Omedetō! Player O won this round with a column 1 domination! :D')
        else: 
            print('Omedetō! Player X won this round with a column 1 domination! :D')
        game_on = False
    if (rowA[1] == 'O' and rowB[1] == 'O' and rowC[1] == 'O') or (rowA[1] == 'X' and rowB[1] == 'X' and rowC[1] == 'X'):
        if rowA[1] == 'O':
            print('Omedetō! Player O won this round with a column 2 domination! :D')
        else: 
            print('Omedetō! Player X won this round with a column 2 domination! :D')
        game_on = False
    if (rowA[2] == 'O' and rowB[2] == 'O' and rowC[2] == 'O') or (rowA[2] == 'X' and rowB[2] == 'X' and rowC[2] == 'X'):
        if rowA[2] == 'O':
            print('Omedetō! Player O won this round with a column 3 domination! :D')
        else: 
            print('Omedetō! Player X won this round with a column 3 domination! :D')
        game_on = False
    
    # Diagonal winning conditions
    if (rowA[0] == 'O' and rowB[1] == 'O' and rowC[2] == 'O') or (rowA[0] == 'X' and rowB[1] == 'X' and rowC[2] == 'X'):
        if rowB[1] == 'O':
            print('Omedetō! Player O finishes with a victorious slash! :D')
        else: 
            print('Omedetō! Player X finishes with a victorious slash! :D')
        game_on = False
    if (rowA[2] == 'O' and rowB[1] == 'O' and rowC[0] == 'O') or (rowA[2] == 'X' and rowB[1] == 'X' and rowC[0] == 'X'):
        if rowB[1] == 'O':
            print('Omedetō! Player O finishes with a victorious backward slash! :D')
        else: 
            print('Omedetō! Player X finishes with a victorious backward slash! :D')
        game_on = False

# Handles tie condition and checks if players want to play another round
def repeat_game():
    global turn_counter
    if turn_counter == 9:
        print('Arara... looks like we have a tie here...')
    res = input('Care to play another round (Y/N)? ')
    if res.lower() == 'y' or res.lower() == 'yes':
        game_on = True
        turn_counter = 0
        init()
    else:
        print('I am sure I will see your beautiful faces again soon!')

# Launch the game!
init()

