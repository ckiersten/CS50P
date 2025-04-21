def main():
    text = ""
    while True or "/" not in text:
        text = input("Fraction: ")
        if convert(text) >= 0:
            break
    print(gauge(convert(text)))


def convert(str):
    try:
        num, denom = str.strip().split("/")
        if denom.isnumeric() and int(denom) == 0:
            raise ZeroDivisionError
        elif not num.isnumeric() or not denom.isnumeric() or int(num) > int(denom):
            raise ValueError
    except (ZeroDivisionError, ValueError):
        return -1
    else:
        num = int(num)
        denom = int(denom)
        return int(round((num / denom)*100))

def gauge(num):
    if num >= 99:
        return "F"
    elif num <= 1:
        return "E"
    else:
        return f"{num}%"

if __name__ == "__main__":
    main()
