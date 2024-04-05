"""
problems.py

Contains all the information and functions for each problems
"""

class Problems:
    def __init__(self, contest_topic, problem_type):
        self.contest_topic = None
        self.problem_type = None
        
        # will be the generation part
        self.problem_statement = None

        pass
    
    def check_ans(self):
        pass

# =======================================
# Specific Problems
# =======================================


class Computer_Number_Systems(Problems):

    def __init__(self, contest_topic, problem_type):
        self.contest_topic = None

        if contest_topic is 0:
            self.problem_statement, self.check_ans = T1_Conversion()
        # elif...

        pass

    

    def T1_Conversion():
        statement = ''
        def check_ans():
            pass

        return statement, check_ans()


    pass