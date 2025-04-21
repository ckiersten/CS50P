import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r'^<iframe.+"(http)s?(://)(?:www.)?(youtube\.com/embed)(.+)"', s):
        a, b, c, d = matches.groups()
        if "s" not in a:
            a = a+"s"
        c = "youtu.be"
        return a+b+c+d
    else:
        return None

if __name__ == "__main__":
    main()
