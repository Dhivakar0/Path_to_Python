BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

current_card = {}
kannada_words_dict = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/kannada_words.csv")
    kannada_words_dict = original_data.to_dict(orient="records")
else:
    kannada_words_dict = data.to_dict(orient="records")
def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(kannada_words_dict)
    kannada_word = current_card["Kannada"]
    canvas.itemconfig(card_title, text="Kannada",fill="black")
    canvas.itemconfig(card_word, text=kannada_word,fill="black")
    canvas.itemconfig(card_background, image=card_front_image)  # Set front image

    # Schedule the flip card to happen in 5 seconds
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=card_back_image)  # Set back image

def is_known():
    kannada_words_dict.remove(current_card)
    known_data = pandas.DataFrame(kannada_words_dict)
    known_data.to_csv("./data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=flip_card)

# Creating a canvas for the flashcards
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)  # Initial image set to front
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons with images
wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Show the first card
next_card()

window.mainloop()






