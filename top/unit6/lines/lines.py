import sys

def main():
    print(count_lines())

def count_lines():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if ".py" not in sys.argv[1]:
            sys.exit("Not a Python file")
        try:
            count = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.lstrip()
                    if not line.startswith("#") and line != "": count += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            return count

if __name__ == "__main__":
    main()
