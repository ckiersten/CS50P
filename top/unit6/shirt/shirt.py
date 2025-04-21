import sys
from PIL import Image, ImageOps
import os

def main():
    shirt()

def shirt():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        root_ext_1 = os.path.splitext(sys.argv[1])
        root_ext_2 = os.path.splitext(sys.argv[2])
        if root_ext_1[1].lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")
        elif root_ext_2[1].lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid output")
        elif root_ext_1[1] != root_ext_2[1]:
            sys.exit("Input and output have different extensions")

        try:
            before = Image.open(sys.argv[1])
            shirt_image = Image.open("shirt.png")
        except FileNotFoundError:
            sys.exit("Input does not exist")
        else:
            size = shirt_image.size
            before = ImageOps.fit(before, size)
            before.paste(shirt_image, shirt_image)
            before.save(sys.argv[2])


if __name__ == "__main__":
    main()
