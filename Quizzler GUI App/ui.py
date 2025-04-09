THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizUi:
    def __init__(self,quiz_brain : QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.score_label = Label(text="Score:0",bg=THEME_COLOR,fg="white",highlightthickness=0,font=("Arial",14,"normal"))
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,width=280,text="Text goes here",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image,highlightthickness=0,command=self.check_true)
        self.right_button.grid(column=0,row=2)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image,highlightthickness=0,command=self.check_false)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have finished the quiz.Check the score above!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)










