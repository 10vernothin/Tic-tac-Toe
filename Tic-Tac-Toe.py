from math import *

"""

This program makes a tic-tac-toe game.

It consists of four helper functions:
    -constructPlayspace() makes the graphics
    -checkStatus() checks if the game ends, and if it's a win or a tie
    -clearSpace() clears the space to default
    -inputIntCheck() checks if the input is int-convertable
    
The main function - game():
    -A number input within 1-9 is entered when prompted
    -Inputting invalid characters will force the player to choose another number
    -The game alternate between "X" and "O"
    -When the game ends, enter "Y"/"y" to play again or the program exits
    
"""


def constructPlayspace(c):
    #this helper function constructs a playspace
    #given the play-space array $c[8]$

    x = " " #blank space
    a = "|" #vertical pylon
    b = "-" #horizontal pylon

    print(x, c[0], a, c[1], a, c[2], x)
    print(14*b)
    print(x, c[3], a, c[4], a, c[5], x)
    print(14*b)
    print(x, c[6], a, c[7], a, c[8], x)


def checkStatus(c, x):
    #this helper function checks if the game wins or ties
    #given the play-space array $c[8]$ and "X" or "O" stri $x$ 
    #returns 1 if $x$ wins, 0 if nothing happens and -1 if it's a tie
    
    win = 0
    used = 0 
    possibilities = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for v in range(0, 8):
        strike = 0
        for w in range(0, 3):
            if (c[possibilities[v][w]] == x):
                strike += 1
        if strike == 3:
            win = 1
    for v in range(0, 8):
        if (type(c[v]) == str):
            used += 1
        if used == 8:
            win = -1
    return win


def clearSpace(c):
    #this helper function clears the playspace
    #of given array c[8]
    for x in range(0, 9):
        c[x] = x+1


def inputIntCheck(n):
    #this helper function is designed to take in inputted Char array $n$
    #and check if the input is able to be converted to Int 
    #will return message:
    # 1 = works
    # 0 = the Char is not int-convertable 
    # -1 = this Char is not 1 char long

    message = 0

    if (len(n) == 1):
        if (47 < ord(n) < 58): #makes sure that they are digits
            message = 1
            return message
    else:
        print("Too many characters. Please choose again:")
        message = -1
        return message
    print("Invalid character. Please choose again:")
    return message


def game():
    #This is the game module

    c = [1, 2, 3, 4, 5, 6, 7, 8, 9] #define playspace
    repetition = "Y"

    print("Let's play a game! 'X' goes first!")
    while (repetition == "Y") or (repetition == "y"):
        print()
        constructPlayspace(c)
        y = "X"
        end =0;
        while end==0:
            print("Please choose a position", y, ":")
            i = 0
            n = 0
            while (i != 1):
                n = input()
                i = inputIntCheck(n)
            n = int(n)
            validity = 0
            while validity == 0:
                if ((0 < n < 10) and (type(c[n-1]) == int )):
                    c[n-1] = y
                    print()
                    constructPlayspace(c)
                    end = checkStatus(c, y)
                    if end == 1:
                        break
                    if (y == "O"):
                        y = "X"
                    else:
                        y = "O"
                    validity = 1;
                else:
                    print("Space already chosen, please choose another number:")
                    j = 0
                    while (j != 1):
                        n = input()
                        j = inputIntCheck(n)
                    n = int(n)
        if (end == 1):
            print()
            print( y, "wins!")
        else:
            print()
            print("It's a tie!")
        clearSpace(c)
        l = input("Would you like to play again? Y or N.")
        repetition = l
        print()
    print("The Game will now end. Thanks for playing!")


#initialization
game()

