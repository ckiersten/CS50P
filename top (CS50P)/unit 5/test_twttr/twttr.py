def main():
    text = input("Input: ").strip()
    print(f"Output: {shorten(text)}")

def shorten(str):
    output = ""
    for ch in str:
        if ch.lower() != "a" and ch.lower() != "e" and ch.lower() != "i" and ch.lower() != "o" and ch.lower() != "u":
            output += ch
    return output

if __name__ == "__main__":
    main()
