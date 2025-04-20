from datetime import date
from datetime import datetime
import inflect
import re
import sys

def main():
    print(amount_minutes(input("Date of Birth: ")))

def amount_minutes(s):
    p = inflect.engine()
    if matches := re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", s):
        y, m, d = matches.groups()
        current = datetime.combine(date.today(), datetime.min.time())
        before = datetime.combine(date.fromisoformat(f"{y}{m}{d}"), datetime.min.time())
        between = current - before
        mins = p.number_to_words(int(between.total_seconds() / 60)).capitalize()
        return f"{mins.replace(" and ", " ")} minutes"
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
