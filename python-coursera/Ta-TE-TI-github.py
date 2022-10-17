# Este es el juego descargado de github original 

# tic tac toe game
import random



# GLOBAL COUNT
count = 0


# function for tic_tac_to_grid
def grid():

    print(turn[6] + "\t|" + turn[7] + "\t|" + turn[8] + "\t")
    print("-" * 15)
    print(turn[3] + "\t|" + turn[4] + "\t|" + turn[5] + "\t")
    print("-" * 15)
    print(turn[0] + "\t|" + turn[1] + "\t|" + turn[2] + "\t")


# function for clear screen
def cls():
    print("\n"*20)


# function for winning condition
def win_case(iput):
    if turn[0] == turn[1] == turn[2] == iput or turn[4] == turn[5] == turn[3] == iput or turn[7] == turn[8] == turn[6] == iput or turn[0] == turn[3] == turn[6] == iput or turn[1] == turn[4] == turn[7] == iput or turn[2] == turn[5] == turn[8] == iput or turn[0] == turn[4] == turn[8] == iput or turn[2] == turn[4] == turn[6] == iput:
        return 1
    else:
        return 0


# function for checking correct input
def check_correct_ip():
    while True:
        try:
            return int(input("your turn : ")) - 1
        except:
            print("enter only digit!")


# function for user_turn
def user_turn(count):
    while count < 9:

        temp = check_correct_ip()
        while turn[temp] != '':
            print("wrong input.Try again")
            temp = int(input("your turn : ")) - 1
        else:
            cls()
            turn[temp] = user
            grid()
            count += 1

            if win_case(user):
                print("Congo!! You win :-)")
                exit(0)
            else:
                com_turn(count)
        print("Match tie!!!")
        exit(0)


# function for computer_turn
def com_turn(count):
    while count < 9:
        temp = random.randint(0, 8)

        while turn[temp] != '':
            temp = random.randint(0, 8)

        cls()
        turn[temp] = computer
        grid()
        count += 1

        if win_case(computer):
            print("Alas! You lose. Better luck next time")
            exit(0)
        else:
            user_turn(count)
        print("Match tie!!!")
        exit(0)


# function decieding who play first
def toss():
    if (input("for first turn press : y")).lower() == 'y':
        user_turn(count)
    else:
        com_turn(count)


# TURN IS THE LIST WHERE THE PLAYER'S INPUT WILL BE KEPT (INITIALYY BLANK)
turn = ['', '', '', '', '', '', '', '', '']


# assign x or o for user  computer to play
user = (input("Enter which sign do you want: X or O ")).upper()
if user == 'X':
    computer = 'O'
elif user == 'O':
    computer = 'X'
else:
    print("Wrong input. Computer take X")
    user = 'O'
    computer = 'X'


# STRAT PLAYING main()
grid()
toss()
