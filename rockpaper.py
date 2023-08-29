import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice = input("Enter your choice = ").lower()


if user_choice == "rock" and computer_choice == "scissors":
    print("You win")

elif user_choice == "scissors" and computer_choice == "paper":
    print("You win")

elif user_choice == "paper" and computer_choice == "rock":
    print("You win")

elif user_choice == computer_choice:
    print("You tied")

else:
    print("You lost")
