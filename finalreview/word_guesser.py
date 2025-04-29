# users guess letters in order to figure out the word
# can you fix the errors?

import tkinter as tk
import random

class WordGuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")

        self.words = ["python", "tkinter", "computer", "program", "developer", "gaming", "algorithm"]
        self.word = "gaming"
        self.guessed_word = "_ _ _ _ _ _"

        self.label = tk.Label(root, text=self.guessed_word, font=("Arial", 18))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Guess", command=self.check_guess, font=("Arial", 14))
        self.submit_button.pack(pady=10)

        self.message_label = tk.Label(root, text="", font=("Arial", 14))
        self.message_label.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get().lower()
        # would be nice if the entry would clear submitting letter

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Enter a single letter!")
            return

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
            self.label.config(text=" ".join(self.guessed_word))
        else:
            self.message_label.config(text=f"'{guess}' is not in the word!")

        if "_" not in self.guessed_word:
            self.message_label.config(text="Congratulations! You guessed the word!")

if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessGame(root)
    root.mainloop()
