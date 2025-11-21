import random

words = ["apple", "train", "robot", "snake", "pizza"]
word = random.choice(words)
word_letters = list(word)
guessed_letters = ["_"] * len(word)
guessed = set()
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_letters))

while wrong_guesses < max_wrong and "_" in guessed_letters:
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single alphabet letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    guessed.add(guess)

    if guess in word_letters:
        print("Correct!")
        for idx, letter in enumerate(word_letters):
            if letter == guess:
                guessed_letters[idx] = guess
    else:
        wrong_guesses += 1
        print("Wrong! Guesses left:", max_wrong - wrong_guesses)
    print("Word:", " ".join(guessed_letters))

if "_" not in guessed_letters:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over. The word was:", word)
