def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(str):
    str = str.strip()
    if len(str) > 6 or len(str) < 2 or not str.isalnum() or str.isnumeric(): return False
    elif str.isalpha(): return True
    else:
        i = 0
        while i <= len(str)-2:
            temp = str[i:i+2]
            if temp[0].isnumeric() and temp[1].isalpha(): return False
            if temp[0].isalpha() and temp[1] == "0": return False
            i += 1
        return True

main()
