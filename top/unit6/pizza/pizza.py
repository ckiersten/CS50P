import csv
import sys
from tabulate import tabulate

def main():
    print(tabulate(table(), headers = "firstrow", tablefmt = "grid"))

def table():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if ".csv" not in sys.argv[1]:
            sys.exit("Not a csv file")
        try:
            menu = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    menu.append({"pizza": row[0], "small": row[1], "large": row[2]})
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            return menu

if __name__ == "__main__":
    main()
