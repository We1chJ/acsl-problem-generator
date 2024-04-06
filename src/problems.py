"""
problems.py

Contains all the information and functions for each problems
"""

import random

class Problems:
    def __init__(self, contest_topic, problem_type):
        self.contest_topic = None
        self.problem_type = None
        self.problem_statement = None
        self.check_ans = None

    def generate_problem(self, problem_type):
        pass

# =======================================
# Specific Problems
# =======================================

# Contest 1 Topic 1: Computer Number Systems
class Computer_Number_Systems(Problems):

    def __init__(self, contest_topic, problem_type):
        self.contest_topic = contest_topic
        self.problem_type = problem_type
        self.problem_statement = None

    def generate_problem(self, problem_type):
        if problem_type == 0:
            self.generate_problem(random.randint(1, 1))
        elif problem_type == 1:            
            self.problem_statement, self.check_ans = self.T1_Conversion()

    # problem type 1: Find the number after convert from one number system to another
    def T1_Conversion(self):
        base_1 = random.choice([2, 8, 16])
        bases = [2, 8, 10, 16]
        bases.remove(base_1)
        base_2 = random.choice(bases)
        num = random.randint(1e4, 1e8)
        ans = num
        if base_1 == 2:
            num = bin(num)[2:]
        elif base_1 == 8:
            num = oct(num)[2:]
        elif base_1 == 16:
            num = hex(num)[2:].upper()
        
        statement = f"Given {num} in base {base_1}, convert it to base {base_2}."

        def check_ans(response):
            return int(response, base_2) == ans

        return statement, check_ans