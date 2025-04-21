import random
import sys

def main():
    guessing()

def guessing():
    while True:
        try:
            lvl = input("Level: ")
        except EOFError:
            print()
            return
        else:
            if not lvl.isnumeric() or int(lvl) < 1:
                continue
            generated = random.randint(1, int(lvl))
            while True:
                try:
                    user_guess = input("Guess: ")
                except EOFError:
                    print()
                    return
                else:
                    if not user_guess.isnumeric() or int(user_guess) < 1:
                        continue
                    if int(user_guess) < generated:
                        print("Too small!")
                    elif int(user_guess) > generated:
                        print("Too large!")
                    else:
                        sys.exit("Just right!")

main()
