from QuestionModel import Question
from QuizData import QuizData
from QuizBrain import QuizBrain
from ui import QuizGUI

question_bank = []

#Creating question bank from the question data
for question in QuizData:
    new_question = Question(question['text'],question['answer'])
    question_bank.append(new_question)

#Creating instance for the quiz brain and quizGUI
quizbrain = QuizBrain(question_bank)
quiz_interface = QuizGUI(quizbrain)




