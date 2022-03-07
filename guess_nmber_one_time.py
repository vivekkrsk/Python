import random

number = random.randint(0,100)

print("Guess a magic number between 1 to 100")

guess = eval(input("Enter your guess: "))

if guess == number:
    print("Yes, the number is",number)
elif guess > number:
    print("Your guess is too high")
else:
    print("Your guess is too low")

print("Correct guess is",number)