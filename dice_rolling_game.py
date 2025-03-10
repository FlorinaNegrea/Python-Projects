import random

counter = 0  

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    
    if choice == 'y':
        try:
            choice2 = int(input('How many dice would you like to roll? '))
            if choice2 <= 0:
                print("Please enter a positive number!")
                continue

            for i in range(choice2):
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                print(f'({die1}, {die2})')
                counter += 1

            print("Total rolls so far:", counter)
        
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif choice == 'n':
        print(f'Thanks for playing! You rolled the dice {counter} times.')
        break

    else:
        print('Invalid choice!')
