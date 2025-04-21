def main():
    text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    text = text.strip().lower()
    num = 0
    if text == "42": num = int(text)
    if num == 42 or text == "forty-two" or text == "forty two": print("Yes")
    else: print("No")

main()
