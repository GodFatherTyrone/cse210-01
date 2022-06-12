import math


def main():
    
    play = input(f'\nDo you want to play a TicTacToe? Yes/No : ')
    play = play.lower()
    if play == "yes":
        gamerestart = True
    else:
        gamerestart = False
    if gamerestart == True:
        game()

    #ENDGAME
    play = input("\nWould you like to play again? Yes/No : ")
    play = play.lower()
    if play == "yes":
        gamerestart = True
    else:
        print("Thank you for playing! ")
        


def game():

    A=1
    B=2
    C=3

    D=4
    E=5
    F=6

    G=7
    H=8
    I=9

    #Start
    print("\nGame Set")
    print(f"{A}|{B}|{C}\n- - -\n{D}|{E}|{F}\n- - -\n{G}|{H}|{I}")
    print("Start")
    gameover = False

    players=["One","Two"]

    while gameover == False:
        for _ in players:
            move = input(f"\nPlayer {_}, where would you like to go? (1-9) ")
        #Player One
            if move == "1" and _ == "One":
                A="X"
            elif move == "2" and _ == "One":
                B="X"
            elif move == "3" and _ == "One":
                C='X'
            elif move == "4" and _ == "One":
                D='X'
            elif move == "5" and _ == "One":
                E='X'
            elif move == "6" and _ == "One":
                F='X'
            elif move == "7" and _ == "One":
                G='X'
            elif move == "8" and _ == "One":
                H='X'
            elif move == "9" and _ == "One":
                I='X'

        #Player Two
            if move == "1" and _ == "Two":
                A="O"
            elif move == "2" and _ == "Two":
                B="O"
            elif move == "3" and _ == "Two":
                C='O'
            elif move == "4" and _ == "Two":
                D='O'
            elif move == "5" and _ == "Two":
                E='O'
            elif move == "6" and _ == "Two":
                F='O'
            elif move == "7" and _ == "Two":
                G='O'
            elif move == "8" and _ == "Two":
                H='O'
            elif move == "9" and _ == "Two":
                I='O'

            #game state
            print(f"{A}|{B}|{C}\n- - -\n{D}|{E}|{F}\n- - -\n{G}|{H}|{I}")
        #EndGame Logic
        #Win conditions: ABC DEF GHI ADG BEH CFI AEI CEG:
        if A=="X" and B=="X" and C=="X" or D=="X" and E=="X" and F=="X" or G=="X" and H=="X" and I=="X" or A=="X" and D=="X" and G=="X" or B=="X" and E=="X" and H=="X" or C=="X" and F=="X" and I=="X" or A=="X" and E=="X" and I=="X" or C=="X" and E=="X" and G=="X":
            print("Player One wins")
            gameover = True
            return
        elif A=="O" and B=="O" and C=="O" or D=="O" and E=="O" and F=="O" or G=="O" and H=="O" and I=="O" or A=="O" and D=="O" and G=="O" or B=="O" and E=="O" and H=="O" or C=="O" and F=="O" and I=="O" or A=="O" and E=="O" and I=="O" or C=="O" and E=="O" and G=="O":
            print("Player Two wins")
            gameover = True
            return
    
main()