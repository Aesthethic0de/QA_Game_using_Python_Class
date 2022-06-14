from QA_model import Question
from questions import question_data

question_bank = []

for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_qa = Question(q_text=question_text, q_ans=question_answer)
    question_bank.append(new_qa)