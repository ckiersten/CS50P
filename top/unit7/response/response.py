import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(str):
    if validators.email(str):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
