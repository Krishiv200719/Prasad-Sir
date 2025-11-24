import random

num = random.randint(100, 999)
chances = 10

while chances > 0:
    guess = int(input("Enter a three-digit number to start the Guess Game: "))
    
    if len(str(guess)) != 3:
        print("Please enter a valid three-digit number.")
        continue
    
    chances -= 1
    guess = int(guess)
    
    if guess == num:
        print("Congratulations! You guessed the correct number!")
        break
    else:
        num_str = str(num)
        guess_str = str(guess)
        correct_digits = 0
        for i in range(3):
            if num_str[i] == guess_str[i]:
                correct_digits += 1

        wrong_position = 0
        for i in range(3):
            if guess_str[i] != num_str[i]:
                if guess_str[i] in num_str:
                    wrong_position += 1

        print(f"Incorrect guess. You have {correct_digits} digit(s) correct and in the correct position.")
        print(f"You also have {wrong_position} digit(s) correct but in the wrong position.")
        print(f"Chances left: {chances}")
        print("Try again!\n")

if chances == 0:
    print("Game over! You've used all your chances.")
    print(f"The correct number was {num}.")