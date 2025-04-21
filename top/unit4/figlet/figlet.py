import sys
import random
from pyfiglet import Figlet

def main():
    change_font()

def change_font():
    figlet = Figlet()
    if len(sys.argv) < 2:
        chosen_font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        try:
            chosen_font = sys.argv[2]
            #check if input name of font
            temp = figlet.getFonts()
            temp.index(chosen_font)
        except IndexError:
            sys.exit("Invalid usage")
    try:
        figlet.setFont(font = chosen_font)
        print(figlet.renderText(input("Input: ")))
    except EOFError:
        print()
        return


main()
