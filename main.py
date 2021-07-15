from art import logo
import random

random_number = random.randint(1, 100)
is_game_over = False

def play_game(attempts):
  print(f"You have {attempts} attempt(s) remaining to guess the number.")
  guess = int(input("Make a guess: "))
  return guess

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == "easy":
  attempts = 10
elif difficulty_level == "hard":
  attempts = 5

while not is_game_over:
  guess = play_game(attempts)
  if guess == random_number:
    print(f"You've got it! The correct answer was {random_number}.")
    is_game_over = True  
  elif guess < random_number:
    print("Too low.\nGuess again.")
  elif guess > random_number:
    print("Too high.\nGuess again.")
  attempts -= 1
  if attempts == 0:
    is_game_over = True
    print("You've run out of guesses, you lose.")
