"""
    Tic Tac Toe game to be played on terminal. The game is played by two individuals. 
    Games starts with an empty 3×3 square grid.  Each player has to input two coordinates, horizontal  and vertical. 
    A player wins drawing 3 consecutive marks either in the horizontal, vertical or diagonal way. 
    Otherwise the game draws when all spots are filled.
"""

def show_grid(game_state):
    """ Print out the square grid and the current state of the game. """    
    output = [state[0] for state in game_state]
    print('-' * 9)
    for z in range(0, 9, 3):
        print('| ' + ' '.join(output[z:z+3])+ ' |')
    print('-' * 9)

def player_in_turn(round):
    """ Print which player is in turn. No return value. """
    player = 'X' if round % 2 == 0 else 'O'
    print(f"Player {player} is your turn.")
    return player

def check_input():
    """ Check user input numbers and return them if everything is ok.
        Return: list with two integers
    """    
    try:
        print("Enter the coordinates.")
        x = int(input("Column number: "))
        y = int(input("Row number: "))
        if x > 3 or y > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            input_numbers = [x, y]   # input convert in integer 
            return input_numbers
    except NameError as error:
        print("Please enter two numbers!")
    except ValueError as error:
        print("Please enter two numbers. One for column and one for row!")

    
if __name__ == "__main__":

    # Game turn, even nr. for gamer_x, odd nr. for gamer_o
    turn = 0  
    # Game over message. It says who wins or Draw
    message = ''
    # Diagonal state
    diagonal_rows = ['', ''] 
    # Game finishes
    game_over = False 
    #  Game table divided by coordinates
    table_coordinates = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]]
    #  table coordinates are empty. Game has not started yet
    game_state = [[' ', coordinates] for coordinates in table_coordinates]

    while not game_over:
        # Printing out the game state in the table
        show_grid(game_state)
        user_input = check_input()
        for game in game_state:   
            if user_input in game and ' ' not in game: # repeat if cell(coordinate) is not empty
                print("This cell is occupied! Choose another one!")
                break
            elif user_input in game and ' ' in game:   # Add X or O depending on turn of gamer
                game[0] = player_in_turn(turn)  # if counter even number -> X gamer otherwise O gamer
                turn += 1 
                # diagonal_rows state
                diagonal_rows[0] = [game_state[0][0], game_state[4][0], game_state[8][0]]  
                diagonal_rows[1] = [game_state[2][0], game_state[4][0], game_state[6][0]]
        #After 5 movements checking results for winner
        if turn >= 5 and turn < 9:
            for i in range(0, 9, 3):
                rows = [game_state[i][0], game_state[i+1][0], game_state[i+2][0]]  # checking if there are three in a row
                if all([row == 'X' for row in rows]):
                    message = "X wins"
                    game_over = True
                    break
                elif all([row == 'O' for row in rows]):
                    message =  "O wins"
                    game_over = True
                    break
            for i in range(0, 3):
                columns = [game_state[i][0], game_state[i+3][0], game_state[i+6][0]]  # checking if there are three in a colunm
                if all([column == 'X' for column in columns]):
                    message = "X wins"
                    game_over = True
                    break
                elif all([column == 'O' for column in columns]):
                    message =  "O wins"
                    game_over = True
                    break  
            for diagonal in diagonal_rows:  
                if all([each == 'X' for each in diagonal]):  # checking if there are three in diagonal_rows
                    message = "X wins"
                    game_over = True
                    break
                elif all([each == 'O' for each in diagonal]):
                    message =  "O wins"
                    game_over = True
                    break 
        elif turn == 9:
            message =  "Draw"
            game_over = True
    
    show_grid(game_state)
    print(message)
