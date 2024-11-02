#Class for creating a question for the question bank
class Question:

    def __init__(self,quiz_question,correct_answer) -> None:
        self.statement = quiz_question
        self.answer = correct_answer