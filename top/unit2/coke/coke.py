def main():
    machine()


def machine():
    due = 50

    while due > 0:
        coin = validInput(due)
        due -= coin

    if due <= 0:
        print(f"Change Owed: {abs(due)}")


def validInput(d):
    while True:
        print(f"Amount Due: {d}")
        c = int(input("Insert Coin: "))
        if c == 25 or c == 10 or c == 5: return c

main()


