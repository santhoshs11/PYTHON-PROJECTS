class q_brain():
    def __init__(self,q_bank):
        self.q_no =0
        self.q_list =q_bank
        self.score =0
    def still_running(self):
        if self.q_no < len(self.q_list):
            return True
        else:
            return False
        
    def new_question(self):
        self.current_question =self.q_list[self.q_no]
        self.q_no += 1
        useranswer = input(f" Q{self.q_no}.{self.current_question.text}  :True/False :")
        self.check_score(useranswer,self.current_question.answer)
    def check_score(self,user,correct):
        if user.lower() ==correct.lower():
            print('you are right!!')
            self.score+=1
            print(f"your score is :{self.score} out of {self.q_no}")
        else:
            print('sorry you are wrong .....')
            self.score-=1
            print(f"your score is :{self.score} out of {self.q_no}")
        print(f"the correct answer is {self.current_question.answer}")        
        