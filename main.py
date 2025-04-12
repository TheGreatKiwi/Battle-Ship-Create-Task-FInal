import random
player = "A"
dashes = "----------------------------------------------------------------------"

#users board
board = [["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-", "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"]]

#Board used to track where user has hit
opp_board = [["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-", "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"]]


#board with computers ships
comp_board = [["-" , "-" ,"-", "b", "b" , "b" , "-" , "-" , "-", "-"],
    ["-" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["b" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "b" , "b"],
    ["b" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["b" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["b" , "-" ,"-", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"b", "-" , "-" , "b" , "b" , "b" , "b" , "b"],
    ["-" , "-" ,"b", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"b", "-" , "-" , "-" , "-" , "-" , "-" , "-"],
    ["-" , "-" ,"b", "-" , "-" , "-" , "-" , "-" , "-" , "-"]]

#Next three functions used to print boards
def print_board():
    print("YOUR BOARD:")
    print(" ", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(str(0) + " " + board[0][0] + " " + board[0][1] + " " + board[0][2] + " " + board[0][3] + " " + board[0][4] + " " + board[0][5] + " " + board[0][6] + " " + board[0][7] + " " + board[0][8] + " " + board[0][9])
    print(str(1) + " " + board[1][0] + " " + board[1][1] + " " + board[1][2] + " " + board[1][3] + " " + board[1][4] + " " + board[1][5] + " " + board[1][6] + " " + board[1][7] + " " + board[1][8] + " " + board[1][9])
    print(str(2) + " " + board[2][0] + " " + board[2][1] + " " + board[2][2] + " " + board[2][3] + " " + board[2][4] + " " + board[2][5] + " " + board[2][6] + " " + board[2][7] + " " + board[2][8] + " " + board[2][9])
    print(str(3) + " " + board[3][0] + " " + board[3][1] + " " + board[3][2] + " " + board[3][3] + " " + board[3][4] + " " + board[3][5] + " " + board[3][6] + " " + board[3][7] + " " + board[3][8] + " " + board[3][9])
    print(str(4) + " " + board[4][0] + " " + board[4][1] + " " + board[4][2] + " " + board[4][3] + " " + board[4][4] + " " + board[4][5] + " " + board[4][6] + " " + board[4][7] + " " + board[4][8] + " " + board[4][9])
    print(str(5) + " " + board[5][0] + " " + board[5][1] + " " + board[5][2] + " " + board[5][3] + " " + board[5][4] + " " + board[5][5] + " " + board[5][6] + " " + board[5][7] + " " + board[5][8] + " " + board[5][9])
    print(str(6) + " " + board[6][0] + " " + board[6][1]+ " " + board[6][2]+ " " + board[6][3] + " " + board[6][4] + " " + board[6][5] + " " + board[6][6] + " " + board[6][7] + " " + board[6][8] + " " + board[6][9])
    print(str(7) + " " + board[7][0] + " " + board[7][1] + " " + board[7][2] + " " + board[7][3] + " " + board[7][4] + " " + board[7][5] + " " + board[7][6] + " " + board[7][7] + " " + board[7][8] + " " + board[7][9])
    print(str(8) + " " + board[8][0] + " " + board[8][1] + " " + board[8][2] + " " + board[8][3] + " " + board[8][4] + " " + board[8][5] + " " + board[8][6] + " " + board[8][7] + " " + board[8][8] + " " + board[8][9])
    print(str(9) + " " + board[9][0] + " " + board[9][1] + " " + board[9][2] + " " + board[9][3] + " " + board[9][4] + " " + board[9][5] + " " + board[9][6] + " " + board[9][7] + " " + board[9][8] + " " + board[9][9])

def print_opp_board():
    print("TRACKING BOARD:")
    print(" ", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(str(0) + " " + opp_board[0][0] + " " + opp_board[0][1] + " " + opp_board[0][2] + " " + opp_board[0][3] + " " + opp_board[0][4] + " " + opp_board[0][5] + " " + opp_board[0][6] + " " + opp_board[0][7] + " " + opp_board[0][8] + " " + opp_board[0][9])
    print(str(1) + " " + opp_board[1][0] + " " + opp_board[1][1] + " " + opp_board[1][2] + " " + opp_board[1][3] + " " + opp_board[1][4] + " " + opp_board[1][5] + " " + opp_board[1][6] + " " + opp_board[1][7] + " " + opp_board[1][8] + " " + opp_board[1][9])
    print(str(2) + " " + opp_board[2][0] + " " + opp_board[2][1] + " " + opp_board[2][2] + " " + opp_board[2][3] + " " + opp_board[2][4] + " " + opp_board[2][5] + " " + opp_board[2][6] + " " + opp_board[2][7] + " " + opp_board[2][8] + " " + opp_board[2][9])
    print(str(3) + " " + opp_board[3][0] + " " + opp_board[3][1] + " " + opp_board[3][2] + " " + opp_board[3][3] + " " + opp_board[3][4] + " " + opp_board[3][5] + " " + opp_board[3][6] + " " + opp_board[3][7] + " " + opp_board[3][8] + " " + opp_board[3][9])
    print(str(4) + " " + opp_board[4][0] + " " + opp_board[4][1] + " " + opp_board[4][2] + " " + opp_board[4][3] + " " + opp_board[4][4] + " " + opp_board[4][5] + " " + opp_board[4][6] + " " + opp_board[4][7] + " " + opp_board[4][8] + " " + opp_board[4][9])
    print(str(5) + " " + opp_board[5][0] + " " + opp_board[5][1] + " " + opp_board[5][2] + " " + opp_board[5][3] + " " + opp_board[5][4] + " " + opp_board[5][5] + " " + opp_board[5][6] + " " + opp_board[5][7] + " " + opp_board[5][8] + " " + opp_board[5][9])
    print(str(6) + " " + opp_board[6][0] + " " + opp_board[6][1]+ " " + opp_board[6][2]+ " " + opp_board[6][3] + " " + opp_board[6][4] + " " + opp_board[6][5] + " " + opp_board[6][6] + " " + opp_board[6][7] + " " + opp_board[6][8] + " " + opp_board[6][9])
    print(str(7) + " " + opp_board[7][0] + " " + opp_board[7][1] + " " + opp_board[7][2] + " " + opp_board[7][3] + " " + opp_board[7][4] + " " + opp_board[7][5] + " " + opp_board[7][6] + " " + opp_board[7][7] + " " + opp_board[7][8] + " " + opp_board[7][9])
    print(str(8) + " " + opp_board[8][0] + " " + opp_board[8][1] + " " + opp_board[8][2] + " " + opp_board[8][3] + " " + opp_board[8][4] + " " + opp_board[8][5] + " " + opp_board[8][6] + " " + opp_board[8][7] + " " + opp_board[8][8] + " " + opp_board[8][9])
    print(str(9) + " " + opp_board[9][0] + " " + opp_board[9][1] + " " + opp_board[9][2] + " " + opp_board[9][3] + " " + opp_board[9][4] + " " + opp_board[9][5] + " " + opp_board[9][6] + " " + opp_board[9][7] + " " + opp_board[9][8] + " " + opp_board[9][9])

def print_comp_board():
    print("OPPONENTS BOARD:")
    print(" ", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(str(0) + " " + comp_board[0][0] + " " + comp_board[0][1] + " " + comp_board[0][2] + " " + comp_board[0][3] + " " + comp_board[0][4] + " " + comp_board[0][5] + " " + comp_board[0][6] + " " + comp_board[0][7] + " " + comp_board[0][8] + " " + comp_board[0][9])
    print(str(1) + " " + comp_board[1][0] + " " + comp_board[1][1] + " " + comp_board[1][2] + " " + comp_board[1][3] + " " + comp_board[1][4] + " " + comp_board[1][5] + " " + comp_board[1][6] + " " + comp_board[1][7] + " " + comp_board[1][8] + " " + comp_board[1][9])
    print(str(2) + " " + comp_board[2][0] + " " + comp_board[2][1] + " " + comp_board[2][2] + " " + comp_board[2][3] + " " + comp_board[2][4] + " " + comp_board[2][5] + " " + comp_board[2][6] + " " + comp_board[2][7] + " " + comp_board[2][8] + " " + comp_board[2][9])
    print(str(3) + " " + comp_board[3][0] + " " + comp_board[3][1] + " " + comp_board[3][2] + " " + comp_board[3][3] + " " + comp_board[3][4] + " " + comp_board[3][5] + " " + comp_board[3][6] + " " + comp_board[3][7] + " " + comp_board[3][8] + " " + comp_board[3][9])
    print(str(4) + " " + comp_board[4][0] + " " + comp_board[4][1] + " " + comp_board[4][2] + " " + comp_board[4][3] + " " + comp_board[4][4] + " " + comp_board[4][5] + " " + comp_board[4][6] + " " + comp_board[4][7] + " " + comp_board[4][8] + " " + comp_board[4][9])
    print(str(5) + " " + comp_board[5][0] + " " + comp_board[5][1] + " " + comp_board[5][2] + " " + comp_board[5][3] + " " + comp_board[5][4] + " " + comp_board[5][5] + " " + comp_board[5][6] + " " + comp_board[5][7] + " " + comp_board[5][8] + " " + comp_board[5][9])
    print(str(6) + " " + comp_board[6][0] + " " + comp_board[6][1]+ " " + comp_board[6][2]+ " " + comp_board[6][3] + " " + comp_board[6][4] + " " + comp_board[6][5] + " " + comp_board[6][6] + " " + comp_board[6][7] + " " + comp_board[6][8] + " " + comp_board[6][9])
    print(str(7) + " " + comp_board[7][0] + " " + comp_board[7][1] + " " + comp_board[7][2] + " " + comp_board[7][3] + " " + comp_board[7][4] + " " + comp_board[7][5] + " " + comp_board[7][6] + " " + comp_board[7][7] + " " + comp_board[7][8] + " " + comp_board[7][9])
    print(str(8) + " " + comp_board[8][0] + " " + comp_board[8][1] + " " + comp_board[8][2] + " " + comp_board[8][3] + " " + comp_board[8][4] + " " + comp_board[8][5] + " " + comp_board[8][6] + " " + comp_board[8][7] + " " + comp_board[8][8] + " " + comp_board[8][9])
    print(str(9) + " " + comp_board[9][0] + " " + comp_board[9][1] + " " + comp_board[9][2] + " " + comp_board[9][3] + " " + comp_board[9][4] + " " + comp_board[9][5] + " " + comp_board[9][6] + " " + comp_board[9][7] + " " + comp_board[9][8] + " " + comp_board[9][9])

#checks if number is between 9-0
def is_valid(num):
    if num > 9 or num < 0:
        print("That coordinate is out of range")
        return False

#Computer randomly guesses a coordinate
def comp_guess():
    while True:
        x_comp_guess = random.randint(0, 9)
        y_comp_guess = random.randint(0, 9)
        if board[y_comp_guess][x_comp_guess] == "b":
            board[y_comp_guess][x_comp_guess] = "x"
            print("Computer hit " + str(x_comp_guess) + ", " + str(y_comp_guess))
            break
        elif comp_board[y_comp_guess][x_comp_guess] == "x" or board[y_comp_guess][x_comp_guess] == "m":
            return False
        elif comp_board[y_comp_guess][x_comp_guess] == "-":
            board[y_comp_guess][x_comp_guess] = "m"
            print("Computer hit " + str(x_comp_guess) + ", " + str(y_comp_guess))
            break

#Takes in users guess for where the ship might be
def user_guess():
    while True:
        x_guess = int(input("What is the x coordinate of your guess? "))
        y_guess = int(input("What is the y coordinate of your guess? "))
        if is_valid(x_guess) is not False and is_valid(y_guess) is not False:
            if comp_board[y_guess][x_guess] == "b":
                print("YOU HIT")
                comp_board[y_guess][x_guess] = "x"
                opp_board[y_guess][x_guess] = "x"
                break
            elif comp_board[y_guess][x_guess] == "x" or comp_board[y_guess][x_guess] == "m":
                print("You already hit that spot")
            elif comp_board[y_guess][x_guess] == "-":
                print("You missed")
                comp_board[y_guess][x_guess] = "m"
                opp_board[y_guess][x_guess] = "m"
                break

#prints a ship vertically
def vertical_ship(x_coord, y_coord, battleship):
    for i in range(len(battleship)):
        board[x_coord + i][y_coord] = battleship[0 + i]

#prints a ship horizontally
def horizontal_ship(x_coord, y_coord, battleship):
    for i in range(len(battleship)):
        board[x_coord][y_coord + i] = battleship[0 + i]

#checks if a ship is horizontal. If it is, it checks if all the indices are valid by putting them into 
#a list and returning false if an index error occurs
def is_valid_h_ship(x_coord, y_coord, h_or_v, battleship):
    check_list = []
    if "Horizontal" in h_or_v or "horizontal" in h_or_v or "HORIZONTAL" in h_or_v or "h" in h_or_v:
        try:
            for i in range(battleship):
                check_list.append(board[x_coord + i][y_coord])
        except IndexError:
            print("Ship out of bounds")
            return False

#Same as previous function but for vertical ships
def is_valid_v_ship(x_coord, y_coord, h_or_v, battleship):
    if "Vertical" in h_or_v or "vertical" in h_or_v or "VERTICAL" in h_or_v or "v" in h_or_v:
        try:
            for i in range(battleship):
                check_list.append(board[x_coord][y_coord + i])
        except IndexError:
            print("Ship out of bounds")
            return False

#lets user pick where there battleships are and makes sure that they choose the right number of ships, etc.
def set_up_board():
    ship_list = []
    for i in range(5):
        while True:
            battleship = ""
            x_coord = int(input("what x coordinate do you want your battleship on? "))
            y_coord = int(input("what y coordinate do you want your battleship on? "))
            h_or_v = input("Do you want it horizontal or vertical? ")
            battleship_input = int(input("What battleship length do you want (between 2 and 5)? "))
            if battleship_lengths(ship_list, battleship_input, i) is not False and is_valid_h_ship(x_coord, y_coord, h_or_v, battleship_input) is not False and is_valid_v_ship(x_coord, y_coord, h_or_v, battleship_input) is not False:
                if battleship_input < 6 and battleship_input > (1):
                    for h in range(battleship_input):
                        battleship += "b"
                if "Horizontal" in h_or_v or "horizontal" in h_or_v or "HORIZONTAL" in h_or_v or "h" in h_or_v:
                    horizontal_ship(y_coord, x_coord, battleship)
                elif "Vertical" in h_or_v or "vertical" in h_or_v or "VERTICAL" in h_or_v or "v" in h_or_v:
                    vertical_ship(y_coord, x_coord, battleship)
                print(" ")
                print_board()
                print(" ")
                ship_list.append(battleship_input)
                break

#Makes sure that user uses all the ship lengths in their five battleships
def battleship_lengths(my_list, battleship_input, num):
    if (battleship_input == 2  and 2 in my_list) or (battleship_input == 3 and 3 in my_list):
        print("You can't have 2 or 3 twice")
        return False
    if num == 4 and 5 not in my_list:
        print("You have to have a 5 length ship")
        return False

#Checks if user or computer wins
def win():
    w2 = 0
    w = 0

    #Checking if player A (user) won
    for i in range(len(comp_board)):
        for h in range(len(comp_board[i])):
            if "b" in comp_board[i][h]:
                w += 1
    if w == 0:
        print("YOU WON!!!")
        return False

    #checking if player B (computer) won
    for i in range(len(board)):
        for h in range(len(board[i])):
            if "b" in board[i][h]:
                w2 += 1
    if w2 == 0:
        print("YOU LOSE!!!")
        return False

#puts all functions together to play game
def play_game():
    global player
    print_board()
    set_up_board()
    while True:
        if player == "A":
            user_guess()
            player = "B"
            print_opp_board()
        elif player == "B":
            print(dashes)
            comp_guess()
            player = "A"
            print_board()
            print(dashes)

        if win() == False:
            print_comp_board()
            break

play_game()
