import inflect

p = inflect.engine()

output = ["Adieu", "adieu"]


def main():
    while True:
        try:
            user_input = input("Name: ").title()
            output.append(user_input)
            new_output = name(user_input)
        except KeyboardInterrupt:
            print()
            print(new_output)
            break


def name(_):
    if len(output) == 3:
        new_output = p.join(output, conj="")
        output[2] = "to " + output[2]
        return new_output
    elif len(output) == 4:
        new_output = p.join(output, final_sep="")
        return new_output
    else:
        new_output = p.join(output)
        return new_output


if __name__ == "__main__":
    main()
