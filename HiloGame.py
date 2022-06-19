import math
import random

def main():
    playhilo()


def playhilo():
    play = True
    score = 300
    while play==True:
        #game output
        number1 = random.choice(range(1,14))
        print(f"\nThe number -{number1}- has been dealt.")
        Input = input(f"Higher of Lower? h/l ")
        number2 = random.choice(range(1,14))
        print(f"\nThe next card is {number2}.")
        #logic
        if number2 > number1 and Input == "h" or number2 < number1 and Input == "l":
            score = score + 100
            print(f"Good job! You now have a score of: {score}")
        else:
            score = score - 70
            print(f"You are wrong, too bad.\nScore = {score}")
        #end
        playagain="y"
        if score > 0:
            playagain= input("Would you like to play again? y/n ")

        if playagain == "n":
            play=False
            print("\nThank you for playing!")
        elif score < 1:
            play=False
            print("\nYou lost! Too bad!")
    return



main()