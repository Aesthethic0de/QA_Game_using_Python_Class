class Quiz_Brain:

    def __init__(self,q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_questions(self):
        current = self.question_list[self.question_no]
        self.question_no += 1
        uanswer = input(f"Q.{self.question_no } : {current.text} (True/False)")
        self.checkanswer(uanswer,current.answer)

    def still_has_questions(self):

        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def checkanswer(self, uanswer, correctanswer):
        if uanswer.lower() == correctanswer.lower():
            self.score += 1
            print("you got the answer right")

        else:
            print("sorry thats wrong answer")

    def check_score(self):
        print(f"the total score is {self.score}")


    def end_message(self):
        print(f"your final score is {self.score} / {len(self.question_list)}")
        print("thankyou for playing this game!!! play again")





