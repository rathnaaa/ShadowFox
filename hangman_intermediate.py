import random

# Hangman visuals for incorrect guesses
hangman_graphics = [
    '''
    ------
    |    |
         |
         |
         |
         |
         |
    ---------
    ''', 
    '''
    ------
    |    |
    O    |
         |
         |
         |
         |
    ---------
    ''',
    '''
    ------
    |    |
    O    |
    |    |
         |
         |
         |
    ---------
    ''',
    '''
    ------
    |    |
    O    |
   /|    |
         |
         |
         |
    ---------
    ''',
    '''
    ------
    |    |
    O    |
   /|\\   |
         |
         |
         |
    ---------
    ''',
    '''
    ------
    |    |
    O    |
   /|\\   |
   /     |
         |
         |
    ---------
    ''',
    '''
    ------
    |    |
    O    |
   /|\\   |
   / \\   |
         |
         |
    ---------
    '''
]

# List of words to choose from
word_list = ["python", "hangman", "challenge", "programming", "development", "computer"]

# Function to display the hangman visual
def display_hangman(tries):
    print(hangman_graphics[tries])

# Function to start the Hangman game
def hangman():
    word = random.choice(word_list)  # Randomly select a word
    word_length = len(word)
    guessed_word = ['_'] * word_length  # List of underscores representing the word
    guessed_letters = []  # List of guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_tries = len(hangman_graphics) - 1  # Maximum incorrect guesses (6)

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 incorrect guesses.")
    print("The word has", word_length, "letters.")
    print("Hint: The word is related to programming.")

    # Game loop
    while incorrect_guesses < max_tries:
        print("\nCurrent Word: " + " ".join(guessed_word))
        print("Incorrect Guesses:", incorrect_guesses)
        display_hangman(incorrect_guesses)
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            # Update the guessed word with the correct guess
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
            print(f"Good job! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! The letter '{guess}' is not in the word.")
        
        # Check if the player has guessed the whole word
        if "_" not in guessed_word:
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame Over! You've run out of tries.")
        print("The word was:", word)

# Run the game
hangman()
