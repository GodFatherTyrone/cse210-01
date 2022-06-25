from distutils.command.build_scripts import first_line_re
import random

def main():
    playagain=True
    out1="_"
    out2="_"
    out3="_"
    out4="_"
    out5="_"
    theguy=[" ___ ","/___","\   /"," \ / ","  O  "," /|\ "," /|\ "]
    wordlist=["guess","seven","colon"]
    word= random.choice(wordlist)
    #print(word)
    letters = word.split()
    for letter in letters:
        first = letter[0]
        second = letter[1]
        third = letter[2]
        forth = letter[3]
        fifth = letter[4]
    #print(f"{first},{second},{third},{forth},{fifth}")
    while playagain == True:
        letterguess=input("Guess a letter form a to z: ")
        letterguess = letterguess.lower()
        if letterguess == first:
            out1 = letterguess
        if letterguess == second:
            out2 = letterguess
        if letterguess == third:
            out3 = letterguess
        if letterguess == forth:
            out4 = letterguess
        if letterguess == fifth:
            out5 = letterguess
        else:
            theguy.pop(0)
            theguy.append("")
            print("Wrong guess")
            if theguy[0] == "  O  ":
                playagain=False

        print(f"{out1} {out2} {out3} {out4} {out5}")
        print(f"\n{theguy[0]}\n{theguy[1]}\n{theguy[2]}\n{theguy[3]}\n{theguy[4]}\n{theguy[5]}\n")
    print("You Lost")







main()