import random

best_score = None  

while True:
    try:
        minim = int(input('Enter the minimum value for the range: '))
        maxim = int(input('Enter the maximum value for the range: '))
        
        if minim >= maxim:
            print("Invalid range! The maximum must be greater than the minimum.")
            continue  

        break  
    except ValueError:
        print("Invalid input! Please enter numbers.")

number_to_guess = random.randint(minim, maxim)

max_attempts = 10
attempts_used = 0  

while max_attempts:
    try:
        guess = int(input(f'Guess the number between {minim} and {maxim} (Attempts left: {max_attempts}): '))
        
        attempts_used += 1  

        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else: 
            print(f'🎉 Congratulations! You guessed the number in {attempts_used} attempts! 🎉')
            
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print("🥇 New Best Score!")

            break  

        max_attempts -= 1 

    except ValueError:
        print("Invalid input! Please enter a number.")

else:
    print(f'❌ You have run out of attempts! The correct number was {number_to_guess}. Better luck next time! ❌')

if best_score is not None:
    print(f'🏆 Best Score: {best_score} attempts!')

