import requests

QuizData = []
NUMBER_OF_QUES = 40  #Number of questions to be retrieved

parameters = {
    "amount":NUMBER_OF_QUES,
    "type": 'boolean',
}

#Retrieving the questions from open trivia DB
#Paramteres as number of question and type of question
response = requests.get(url='https://opentdb.com/api.php',params=parameters)
data = response.json()

#Constructing a list of questions with answer 
for index in range(NUMBER_OF_QUES):
    ques_dict = {
        "text": data['results'][index]['question'],
        "answer": data['results'][index]['correct_answer']
    }
    QuizData.append(ques_dict)
