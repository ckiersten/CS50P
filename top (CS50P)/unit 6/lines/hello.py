def main():
    print(hello())

def hello():
    name = input("What's your name? ")
    hi_str = "hello " + name
    return hi_str

if __name__ == "__main__":
    main()
