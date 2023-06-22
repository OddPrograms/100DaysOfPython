# class User:
#     def __init__(self, id, username):
#         print("New user being created...")
#         self.id = id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User("001", "John")
# user_2 = User("002", "Jane")
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
#
# print(user_2.followers)
# print(user_2.following)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [
    # Question(question_data[0]["text"], question_data[0]["answer"]),
    # Question(question_data[1]["text"], question_data[1]["answer"]),
    # Question(question_data[2]["text"], question_data[2]["answer"]),
    # Question(question_data[3]["text"], question_data[3]["answer"]),
    # Question(question_data[4]["text"], question_data[4]["answer"]),
    # Question(question_data[5]["text"], question_data[5]["answer"]),
    # Question(question_data[6]["text"], question_data[6]["answer"]),
    # Question(question_data[7]["text"], question_data[7]["answer"]),
    # Question(question_data[8]["text"], question_data[8]["answer"]),
    # Question(question_data[9]["text"], question_data[9]["answer"]),
    # Question(question_data[10]["text"], question_data[10]["answer"])
]

'''Loops through the question_data to fill question_bank. More efficient than above.'''
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# for question in question_bank:
#     print(question.text)
#     print(question.answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")