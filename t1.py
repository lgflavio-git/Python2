import random

computer_number = random.randint(1, 100)

while True:
    guess_answer = int(input("Guess a number between 1 and 100 :"))
    if 1 <= guess_answer <= 100: 
        print("valid Number")
        break
    else:
        print("Invalid Number")


2