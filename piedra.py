import random
choices = ('r','s','p')

user_choice = input("piedra, papel o tijera. (r/p/s) :").lower()
if user_choice not in choices :
    print ("Error")

computer_choice = random.choices(choices)
print (f"your choice {user_choice}")
print (f"Computer choice {computer_choice}")

if user_choice == computer_choice:
    print ("same")

