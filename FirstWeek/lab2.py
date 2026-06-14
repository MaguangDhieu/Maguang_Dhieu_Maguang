sercret_number = 42
guess = int(input("Guess the secret number: "))
if guess < secret_number:
    print("Too low! Try again.")
elif guess > secret_number:
    print("Too high! Try again.")
else:
    print("Congratulations! You guessed the secret number.")