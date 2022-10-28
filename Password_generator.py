import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main():
    global ask_number

    print("Générateur de mot de passe:")
    try:
        ask_number = int(input("Combien de caractères composent ton mot de passe ? (0 - 20)"))
    except ValueError:
        print("Choisis un nombre !")
        main()

    ask_upper = str(input("Veux-tu des majuscules ?"))

    ask_num = str(input("Veux-tu des chiffres ?"))

    if ask_upper == "oui" and ask_num == "oui":
        uppercase_numbers()
    if ask_upper == "non" and ask_num == "non":
        no_uppercase_no_numbers()
    if ask_upper == "oui" and ask_num == "non":
        uppercase_no_numbers()
    if ask_upper == "non" and ask_num == "oui":
        no_uppercase_numbers()


def no_uppercase_no_numbers():
    for i in range(0, ask_number):
        digit = random.randint(0, 25)
        print(alphabet[digit], end="")


def uppercase_no_numbers():
    for i in range(0, ask_number):
        uppercase = random.randint(0, 1)
        digit = random.randint(0, 25)
        if uppercase == 0:
            print(alphabet[digit], end="")
        elif uppercase == 1:
            print(alphabet[digit].upper(), end="")


def no_uppercase_numbers():
    for i in range(0, ask_number):
        digit = random.randint(0, 25)
        num = random.randint(0, 9)
        num_or_not = random.randint(0, 2)

        if num_or_not != 1:
            print(alphabet[digit], end="")
        elif num_or_not == 1:
            print(numbers[num], end="")


def uppercase_numbers():
    for i in range(0, ask_number):
        digit = random.randint(0, 25)
        num = random.randint(0, 9)
        num_or_not = random.randint(0, 2)
        uppercase = random.randint(0, 1)

        if num_or_not != 1:
            if uppercase == 0:
                print(alphabet[digit], end="")
            elif uppercase == 1:
                print(alphabet[digit].upper(), end="")
        elif num_or_not == 1:
            print(numbers[num], end="")


if __name__ == '__main__':
    main()
