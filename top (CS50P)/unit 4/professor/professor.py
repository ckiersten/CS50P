import random

def main():
    correct = 0
    l = get_level()
    i = 0
    while i < 10:
        x = generate_integer(l)
        y = generate_integer(l)
        tries = 0
        while True:
            answer = input(f"{x} + {y} = ")
            if not answer.isnumeric() or int(answer) != x + y:
                tries += 1
                print("EEE")
                if tries == 3:
                    print(f"{x} + {y} = {x+y}")
                    break
                continue
            else:
                correct += 1
                break
        i += 1
    print(f"Score: {correct}")



def get_level():
    while True:
        lvl = input("Level: ")
        if not lvl.isnumeric() or int(lvl) < 1 or int(lvl) > 3:
            continue
        else:
            break
    return int(lvl)


def generate_integer(level):
    upper_limit = (10 ** level) -1
    if level == 1:
        lower_limit = 0
    else:
        lower_limit = 10 ** (level -1)
    #upper_limit = (10 ** level) -1
    return random.randint(lower_limit, upper_limit)


if __name__ == "__main__":
    main()
