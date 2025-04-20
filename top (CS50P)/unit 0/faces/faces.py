def convert(str):
    output = str.replace(":)", "🙂")
    output = output.replace(":(", "🙁")
    return output

def main():
    text = input("turn emoticons to emojis")
    print(convert(text))

main()
