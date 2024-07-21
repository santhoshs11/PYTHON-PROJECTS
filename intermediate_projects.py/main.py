from questionmodel import Question
from data_quiz import question_data
from quizbrain import q_brain
question_list =[]
for question in question_data:
    q_text =question["text"]
    q_answer = question["answer"]
    new_q = Question(q_text,q_answer)
    question_list.append(new_q)
   
quiz =q_brain(question_list)
while quiz.still_running():
    quiz.new_question()
print("YOU COMPLETE THE QUIZ")
print(f'your final score is {quiz.score}/{quiz.q_no}')    