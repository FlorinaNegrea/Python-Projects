import random

choices = ('r', 'p', 's')
emojis = {'r': '🪨', 's' : '✂️', 'p' : '📄' }

total_wins = 0
total_losses = 0
total_ties = 0

while True:
    users_games_won = 0
    computer_games_won = 0 

    print ('Best of 3 - First to 2 wins')
    while users_games_won < 2 and computer_games_won < 2:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice not in choices:
            print('Invalid choice')
            continue
        computer_choice = random.choice(choices)

        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[computer_choice]}')

        if user_choice == computer_choice:
            print('Tie!')
            total_ties += 1
        elif (
            (user_choice == 'r' and computer_choice == 's') or 
            (user_choice == 's' and computer_choice == 'p') or 
            (user_choice == 'p' and computer_choice == 'r')):
            print('You win')
            users_games_won += 1
        else:
            print('You lose')
            computer_games_won += 1

        print(f'Score: You {users_games_won} - {computer_games_won} Computer')
        
    if users_games_won == 2:
        print('Congratulations! You are the overall winner!')
        total_wins += 1
    else:
        print('Computer is the overall winner! Better luck next time!')
        total_losses += 1

    while True:
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue in ('y', 'n'):
            break
        print("Invalid choice! Please enter 'y' for Yes or 'n' for No.")

    if should_continue == 'n':
        print(' Game Over! Here are your final stats:')
        print(f' Total Wins: {total_wins}')
        print(f' Total Losses: {total_losses}')
        print(f' Total Ties: {total_ties}')
        print("Thanks for playing! ")
        break