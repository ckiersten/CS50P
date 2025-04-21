import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^([1-9][0-2]?)(.+)(AM|PM) to ([1-9][0-2]?)(.+)(AM|PM)$", s):
        a1, a2, a3, b1, b2, b3 = matches.groups()
        a2 = a2.strip()
        b2 = b2.strip()

        if len(a2) > 0 and a2[1:].isnumeric():
            if int(a2[1:]) > 59:
                raise ValueError
        elif len(b2) > 0 and b2[1:].isnumeric():
            if int(b2[1:]) > 59:
                raise ValueError

        if len(a2) == 0:
            a2 = ":00"
        if len(b2) == 0:
            b2 = ":00"

        if a3 == "AM":
            if int(a1) == 12:
                a1 = "00"
            else:
                a1 = f"{int(a1):02}"
            time1 = a1+a2
        else:
            if int(a1) != 12:
                a1 = int(a1) + 12
            time1 = f"{a1}{a2}"

        if b3 == "AM":
            if int(b1) == 12:
                b1 = "00"
            else:
                b1 = f"{int(b1):02}"
            time2 = b1+b2
        else:
            if int(b1) != 12:
                b1 = int(b1) + 12
            time2 = f"{b1}{b2}"

        return time1+" to "+time2

    else:
        raise ValueError

if __name__ == "__main__":
    main()
