import random

print("WELCOME TO THE RANDOM NUMBER GUESSING GAME")
print("YOU HAVE TO ENTER ANY NUMBER BETWEEN 1 TO 100...LET'S SEE IF YOU CAN GUESS IT!!")

random_num = random.randint(1, 100)

attempts = 0
guess_num = None

while guess_num != random_num:
    guess_num = int(input("Enter your number: "))
            

    if guess_num < 1 or guess_num > 100:
        print("Number out of range")
        continue

    attempts += 1

    if guess_num < random_num:
        print("Going low...Try Again!")

    elif guess_num > random_num:
        print("Going high...Try Again!")

    else:
        print(f"CONGRATULATIONS!!! YOU HAVE GUESSED IT RIGHT IN {attempts} ATTEMPTS")
