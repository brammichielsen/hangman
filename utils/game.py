class hangman:
# Create a Hangman class

    possible_words = ["becode", "learning", "mathematics", "sessions"]
    # possible_words attribute contains a list of words that could need to be guessed

    def __init__(self):
        self.word_to_find = []
        # word_to_find attribute is a list that contains each letter of the word as a string
        
        self.lives = 5
        # lives attribute starts at 5 and contains number of lives left

        self.correctly_guessed_letters = []
        # correctly_guessed_letters attribute is a list of strings with guessed letters
        # starts with underscores representing all non-guessed letters in the word
        # all places where a letter appears should be shown at the same time when guessed

        self.wrongly_guessed_letters = []
        # wrongly_guessed_letters attribute is a list of strings with incorrect letters
        # these letters are NOT in word_to_find 

        self.turn_count = 0
        # turn_count attribute is an integer indicating number of turns played

        self.error_count = 0
        # error_count attribute is an integer indicating number of errors made


    def play(self):
        letter = input("Enter a letter: ")
        # play() method asks the player to enter a letter

        if letter.isalpha() and len(letter) == 1:
        # player should be only allowed to type a letter, and no more than one

            if letter in self.word_to_find:
                indices = []
                # Create an empty list to store the indices where the letter appears
    
                for i in range(len(self.word_to_find)):
                    if self.word_to_find[i] == letter:
                        indices.append(i)
                # Iterate over the indices of the word_to_find and check if the character at that index is equal to the guess letter.
                # If it matches, add the index to the indices list.
    
                for index in indices:
                    self.correctly_guessed_letters[index] = letter
                # Update the correctly_guessed_letters at the corresponding indices with the guess letter.

            else:
                self.wrongly_guessed_letters.append(letter)
                self.error_count += 1
                self.lives -= 1
            # an incorrectly guessed letter gets added to wrongly_guessed_letters
            # error_count +1
            # lives -1

        else:
            print("Please enter a valid letter.")

    def start_game(self):
        self.word_to_find = list(self.possible_words[0])
        # Choose a word from possible_words
        
        self.correctly_guessed_letters = ['_' for _ in self.word_to_find]  
        # Initialize with underscores

        print(" ".join(self.correctly_guessed_letters))
        # Display initial word
        
        while self.lives > 0 and '_' in self.correctly_guessed_letters and self.correctly_guessed_letters != self.word_to_find:
            self.turn_count += 1
            self.play()
            # start_game() method calls play() until the player wins or loses

            self.print_status()
            # start_game() method calls print_status to print correctly_guessed_letters, wrongly_guessed_letters, lives, error_count and turn_count at the end of each turn

        if self.lives == 0:
            self.game_over()
            # game_over() method stops the game and prints "Game over...""

        else:
            self.well_played()
            # well_played() method prints 'You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!'


    def print_status(self):
        print(f"Correctly Guessed Letters: {' '.join(self.correctly_guessed_letters)}")
        print(f"Wrongly Guessed Letters: {' '.join(self.wrongly_guessed_letters)}")
        print(f"Lives: {self.lives}")
        print(f"Error Count: {self.error_count}")
        print(f"Turn Count: {self.turn_count}")
        print("\n")
    # print_status() prints correctly_guessed_letters, wrongly_guessed_letters, lives, error_count and turn_count followed by a blank line

    def game_over(self):
        print("Game Over...")


    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")