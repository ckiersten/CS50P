def main():
    f = fuel_gauge()
    if f >= 99:
        print("F")
    elif f <= 1:
        print("E")
    else:
        print(f"{f}%")


def fuel_gauge():
    while True:
        try:
            num, denom = input("Fraction: ").strip().split("/")
            num = int(num)
            denom = int(denom)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if num > denom:
                pass
            else: return int(round((num / denom)*100))

main()
