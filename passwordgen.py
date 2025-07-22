import random
import string

characters = list(string.ascii_letters)

def passGen(password = ""):
    while True:

        password += str(random.randint(1 ,12))

        password += random.choice(characters)

        if len(password) > 10:
            return password

def main():
    print("Your password is: ", end="")
    print(passGen())

if __name__ == "__main__":
    main()