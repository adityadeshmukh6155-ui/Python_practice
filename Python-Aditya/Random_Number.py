import random

secret_number = random.randint(1,10)

name = input("inter your name  ")

while True:
    number = int(input("guess the number in between  1 to 10\n"))

    if number == secret_number:
        print("you are correct",name)
        break

    elif number <  secret_number:
        print("too low")

    else:
        print("too high")