import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"^(\d+\d?\d?\.)(\d+\d?\d?\.)(\d+\d?\d?\.)(\d+\d?\d?)$", ip):
        a, b, c, d = matches.groups()
        a = int(a[:len(a)-1])
        b = int(b[:len(b)-1])
        c = int(c[:len(c)-1])
        d = int(d)
        if a <= 255 and b <= 255 and c <= 255 and d <= 255:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
