from QA_model import Question
from questions import question_data
from quiz_brains import Quiz_Brain
from combine_qa import question_bank

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_questions()
    quiz.check_score()
quiz.end_message()






