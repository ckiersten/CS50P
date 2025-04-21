def main():
    text = input("What time is it? ")
    text = text.strip()
    dec = convert(text)
    if dec >= 7 and dec <= 8:
        print("breakfast time")
    elif dec >= 12 and dec <= 13:
        print("lunch time")
    elif dec >= 18 and dec <= 19:
        print("dinner time")


def convert(time):
    hr, min = time.split(":")
    hr = float(hr)
    if min.endswith("a.m."):
        min = min[:min.find("a")]
    elif min.endswith("p.m."):
        hr += 12
        min = min[:min.find("p")]
    min = float(min) / 60
    return hr + min

if __name__ == "__main__":
    main()
