import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    list_um = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(list_um)

if __name__ == "__main__":
    main()
