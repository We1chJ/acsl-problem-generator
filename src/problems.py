"""
problems.py

Contains all the information and functions for each problems
"""

import random

class Problems:
    def __init__(self):
        self.contest_topic = None
        self.problem_type = None
        self.problem_statement = None
        self.ans = None

    def generate_problem(self):
        pass

    def check_ans(self, response):
        return self.ans == response

# =======================================
# Specific Problems
# =======================================

# Contest 1 Topic 1: Computer Number Systems
class Computer_Number_Systems(Problems):
    
    NUMBER_OF_PROBLEM_TYPES = 1

    def __init__(self, contest_topic, problem_type):
        self.contest_topic = contest_topic
        self.problem_type = problem_type
        self.problem_statement = None

    def generate_problem(self, problem_type):
        if problem_type == 0:
            self.generate_problem(random.randint(1, Computer_Number_Systems.NUMBER_OF_PROBLEM_TYPES))
        elif problem_type == 1:
            self.problem_statement, self.ans = self.T1_Conversion()

    # problem type 1: Find the number after convert from one number system to another
    def T1_Conversion(self):
        base_start = random.choice([2, 8, 16])
        bases = [2, 8, 10, 16]
        bases.remove(base_start)
        base_result = random.choice(bases)
        num = random.randint(1e4, 1e8)
        ans = num
        if base_start == 2:
            num = bin(num)[2:]
        elif base_start == 8:
            num = oct(num)[2:]
        elif base_start == 16:
            num = hex(num)[2:].upper()
        
        statement = f"Given {num} in base {base_start}, convert it to base {base_result}."

        if base_result == 2:
            ans = bin(ans)[2:]
        elif base_result == 8:
            ans = oct(ans)[2:]
        elif base_result == 16:
            ans = hex(ans)[2:]

        return statement, ans