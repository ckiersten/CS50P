import emoji

def main():
    try:
        text = input("Input: ")
    except EOFError:
        print()
        return 
    else:
        print(f"Output: {emoji.emojize(text, language = 'alias')}")

main()
