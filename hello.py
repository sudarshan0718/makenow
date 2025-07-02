import random

def get_user_choice():
    choices = ['stone', 'paper', 'scissor']
    user_input = input("Enter your choice (stone, paper, scissor): ").lower()
    while user_input not in choices:
        print("Invalid choice. Try again.")
        user_input = input("Enter your choice (stone, paper, scissor): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissor'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'stone' and computer == 'scissor') or \
         (user == 'paper' and computer == 'stone') or \
         (user == 'scissor' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()