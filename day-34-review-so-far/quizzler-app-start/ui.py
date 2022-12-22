from tkinter import *
from quiz_brain import QuizBrain




THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image= true_img, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image= false_img, command=self.true_pressed)
        self.false_button.grid(column=1, row=2)
        self.score_label = Label(text="Score:", font=(FONT_NAME, 20, "bold"))
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125, width=280,text="Some question", fill=THEME_COLOR, font=(FONT_NAME, 20, "italic"))
        
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


