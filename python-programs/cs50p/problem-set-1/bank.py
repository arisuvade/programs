forbidden_letter = "h"
forbidden_greeting = "hello"

greeting = input("Greeting: ").lower()

if greeting == forbidden_greeting:
    print("$0")
elif (forbidden_letter in greeting[0] and
      forbidden_greeting not in greeting):
    print("$20")
elif greeting >= forbidden_greeting:
    print("$0")
else:
    print("$100")
