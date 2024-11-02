from tkinter import *
from QuizBrain import QuizBrain

THEME_COLOR = "#375362"

class QuizGUI:
    
    #Initializing a gui
    def __init__(self,quizbrain:QuizBrain) -> None:
        self.quizbrain = quizbrain
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.configure(bg=THEME_COLOR,padx=20,pady=20,height=350,width=400)

        self.score_label = Label(text="Score:0",background=THEME_COLOR,fg='white',font=('Ariel',10,'italic'))
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250,background='white')
        self.canvas_text = self.canvas.create_text(150,125,text="",font=('Ariel',15,'italic'),fill=THEME_COLOR,width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=30)

        self.wrong_image = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=self.wrong_image,borderwidth=0,highlightthickness=0,command=self.set_false)
        self.wrong_button.grid(column=1,row=2)

        self.right_image = PhotoImage(file='./images/true.png')
        self.right_button = Button(image=self.right_image,borderwidth=0,highlightthickness=0,command=self.set_true)
        self.right_button.grid(column=0,row=2)

        self.display_question()

        self.window.mainloop()

    #Function to display the questions till there are questions in the question bank
    def display_question(self):
        self.canvas.config(background='white')
        if(self.quizbrain.is_ques_left()):
            ques,ques_no = self.quizbrain.next_question()
            self.canvas.itemconfig(self.canvas_text,text=f"Q.{ques_no}:{ques}",fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.canvas_text,text="You have reached the end of the quiz!!!")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    #Function triggers after clicling tick button and is checked against correct answer
    def set_true(self):
        ans= self.quizbrain.is_answer_correct("True")
        self.feedback(ans)
        self.score_label.config(text=f"Score:{self.quizbrain.score}")

    #Function triggers after clicling cross button and is checked against wrong answer
    def set_false(self):
        ans= self.quizbrain.is_answer_correct("False")
        self.feedback(ans)
        self.score_label.config(text=f"Score:{self.quizbrain.score}")

    #Function to make screen green when answer is right and red when answer is wrong
    def feedback(self,answer):
        if(answer):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.display_question)