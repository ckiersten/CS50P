import inflect

def main():
    p = inflect.engine()
    print(f"Adieu, adieu, to {p.join(list_names())}")

def list_names():
    names = []
    while True:
        try:
            text = input("Name: ")
            names.append(text)
        except EOFError:
            print()
            return names

main()
