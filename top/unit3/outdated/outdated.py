def main():
    convert_dates()

def convert_dates():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            text = input("Date: ").strip().title()
            if "," in text:
                month, day, year = text.split(" ")
                if month.isnumeric():
                    continue
                month = months.index(month)+1
                day = day[:len(day)-1]
        except IndexError:
            pass
        except EOFError:
            print()
            break
        else:
            if "/" in text:
                month, day, year = text.split("/")
                if not month.isnumeric() or not day.isnumeric() or not year.isnumeric():
                    continue
                elif int(month) > 12:
                    continue
            elif "," not in text:
                continue
            if int(day) > 31:
                continue
            print(f"{year}-{month:>02}-{day:>02}")
            return 

main()

