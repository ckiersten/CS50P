import sys
import csv

def main():
    scourgify()

def scourgify():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            students = []
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append({"name": row["name"], "house": row["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
        else:
            with open(sys.argv[2], "w") as new_file:
                writer = csv.DictWriter(new_file, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for student in students:
                    last, first = student["name"].split(",")
                    first = first.lstrip()
                    writer.writerow({"first": first, "last": last, "house": student["house"]})



if __name__ == "__main__":
    main()
