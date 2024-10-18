from question_model import Question
from data import question_data
from newdata import open_trivia_questions
from quiz_brain import QuizBrain

question_bank = []

#Adding questions from course materials to the question bank
for question in question_data:
    new_question = Question(question['text'],question['answer'])
    question_bank.append(new_question)

#Adding questions from open trivia DB API to the question bank
for question in open_trivia_questions:
    new_question = Question(question['question'],question['correct_answer'])
    question_bank.append(new_question)

#Creating object for the conducting a quiz
quiz = QuizBrain(question_bank)

#Keep running quiz until there are questions in question bank
#Getting next question, checking if user's answer is correct and display intermediate score
while quiz.still_has_ques():
    current_answer = quiz.next_question()
    quiz.is_answer_correct(current_answer)
    print(f"Your current score is :{quiz.get_score()}/{quiz.question_number}")
    print()

#Displaying final score 
print("You've completed the quiz.")
print(f"Your final score is :{quiz.get_score()}/{quiz.question_number}")