import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    if matches:
        link = "https://youtu.be/" + matches.group(1)
        return link
    else:
        return None


...


if __name__ == "__main__":
    main()
