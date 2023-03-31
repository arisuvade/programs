import sys
from PIL import Image, ImageOps


def main():
    first, second = arg_counter()
    first_file, second_file = ext_validator(first, second)
    image_edit(first_file, second_file)


def arg_counter():
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def ext_validator(first, second):
    if first.endswith(".jpg") or first.endswith(".png"):
        if second.endswith(".jpg") or second.endswith(".png"):
            if (first.endswith(".jpg") and second.endswith(".jpg") or
                    first.endswith(".png") and second.endswith(".png")):
                return first, second
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")
    else:
        sys.exit("Invalid output")


def image_edit(first, second):
    try:
        user_image = Image.open(first)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    user_image = ImageOps.fit(user_image, size)
    user_image.paste(shirt, shirt)
    user_image.save(second)
    return user_image


if __name__ == "__main__":
    main()
