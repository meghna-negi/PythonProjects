import html

class QuizBrain:
    def __init__(self,question_list) -> None:
        self.question_number = 0            #Question number
        self.question_list = question_list  #Question bank
        self.score = 0                      #Initializing the score of the user

    #Function to check if there are any remaining questions
    def is_ques_left(self):
        return(self.question_number < len(self.question_list))
    
    #Function to check if answer is correct and increase the score accordingly
    def is_answer_correct(self, current_answer):
        if(self.question_list[self.question_number-1].answer.lower() == current_answer.lower()):
            self.score += 1
            print("You got it right!!")
            return(True)
        else:
            print("That's wrong.")
            return(False)

    #Function to get the next question from the question bank
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(question.statement)
        return(q_text,self.question_number)
    
    #Function to get the user's score
    def get_score(self):
        return(self.score)