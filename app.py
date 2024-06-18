# Import random library.
import random

if __name__ == '__main__':
    # Make a python dictionary with keys 'rock', 'paper', 'scissors' and values as -1,0,1 respectively. Name the variable as choice
    choice = {'rock': -1, 'paper': 0, 'scissors': 1}
    # Initialize variables indicating number of wins for user and computer to 0. Name the variables as user_wins and computer_wins.
    user_wins = 0
    computer_wins = 0

    # Initialize a round counter variable to 0. Name the variable as round_counter. Initialize a stop variable to False. Name the variable as stop. Make a while loop till stop is False.
    round_counter = 0
    stop = False
    while not stop:
        # Increment the round counter by 1.
        round_counter += 1

        # Print the round number.
        print('Round', round_counter)

        # Print available choices.
        print('Available choices:', ', '.join(choice.keys()))

        # Make the computer choose randomly from the keys of the choice dictionary. Name the variable as computer_choice.
        computer_choice = random.choice(list(choice.keys()))

        # Ask the user to input a choice. Name the variable as user_choice.
        user_choice = input('Enter your choice: ')

        # Check if the user_choice is 'rock', 'paper' or 'scissors'. If not, print 'Invalid choice' and continue taking input till the user gives a valid input.
        while user_choice not in choice.keys():
            print('Invalid choice')
            user_choice = input('Enter your choice: ')

        # Print the computer's choice.
        print('Computer chooses:', computer_choice)

        # Print the user's choice.
        print('You choose:', user_choice)

        # Calculate the result by subtracting computer's choice from user's choice. Name the variable as result.
        result = choice[user_choice] - choice[computer_choice]

        # Check if the result is 0. If so, print 'It's a tie'.
        if result == 0:
            print("It's a tie")

        # Check if the result is 1 or -2. If so, print 'You win'.
        elif result == 1 or result == -2:
            print('You win')
            user_wins += 1

        # If the above conditions are not met, print 'Computer wins'.
        else:
            print('Computer wins')
            computer_wins += 1

        # Ask the user if they want to play again. If they say no, set stop to True.
        play_again = input('Do you want to play again? (yes/no) ')
        
        # Run while loop to check whether the user has entered a valid input. If not, ask the user to enter a valid input.
        while play_again.strip().lower() not in ['yes', 'no']:
            print('Invalid input')
            play_again = input('Do you want to play again? (yes/no) ')
        if play_again.strip().lower() == 'no':
            stop = True
    
    # Print the number of rounds and the number of wins for user and computer.
    print('Number of rounds:', round_counter)
    print('Number of wins for user:', user_wins)
    print('Number of wins for computer:', computer_wins)
