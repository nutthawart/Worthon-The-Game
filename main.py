# Library ที่จำเป็น
import enum
from tkinter import *
from tkinter import messagebox
import random

# Color Scheme
GREEN = "#538d4e"
YELLOW = "#b59f3b"
BLACK = "#3a3a3c"
WHITE = "#ffffff"
BACKGROUND = "#121213"

# สร้างหน้าต่าง
root = Tk()
root.title("Worthon The Game")
root.resizable(False, False)

# เก็บคำที่ต้องเดาไว้ในตัวแปร
word = random.choice(open("words.txt").read().split())
print(word)

root.config(bg=BACKGROUND)

guessnum = 1

wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)


def getGuess():

  global word
  guess = wordInput.get().lower()

  global guessnum

  if guessnum <= 5:

    if len(guess) == 5:

      if word == guess:  #CORRECT
        for i, letter in enumerate(guess):
          label = Label(root, text=letter.upper(), font=("Arial", 20, "bold"))
          label.grid(row=guessnum, column=i, padx=10, pady=10)
          label.config(bg=GREEN, fg=WHITE)
        messagebox.showinfo("Correct!",
                            f"You win, Congrats! the word was {word.title()}")
      else:  #INCORRECT
        for i, letter in enumerate(guess):

          label = Label(root, text=letter.upper(), font=("Arial", 20, "bold"))
          label.grid(row=guessnum, column=i, padx=10, pady=10)

          if letter == word[i]:  #if they get the letter right
            label.config(bg=GREEN, fg=WHITE)

          if letter in word and not letter == word[
              i]:  #if the letter is in the word, but not in the right spot
            label.config(bg=YELLOW, fg=WHITE)

          if letter not in word:
            label.config(bg=BLACK, fg=WHITE)

    else:
      messagebox.showerror("Use 5 characters",
                           "Please use 5 characters in your guess")

  else:
    messagebox.showerror("Wrong!", f"You Lose! The word was {word}")

  guessnum += 1


wordGuessButton = Button(root, text="Guess", command=getGuess)
wordGuessButton.grid(row=999, column=3, columnspan=2)

root.mainloop()
