def main():
    text = input("camelCase: ")
    text = text.strip()
    toSnakeCase(text)

def toSnakeCase(str):
    output = ""
    for ch in str:
        temp = ch
        if ch.isupper():
            output += "_"
            temp = ch.lower()
        output += temp
    print(output)

main()
