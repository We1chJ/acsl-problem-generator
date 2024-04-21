"""
problems.py

Contains all the information and functions for each problems
"""

import random
import numpy as np

class Problems:
    def __init__(self, contest_topic, problem_type):
        self.contest_topic = contest_topic
        self.problem_type = problem_type
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

    def generate_problem(self, problem_type):
        if problem_type == 0:
            self.generate_problem(random.randint(1, Computer_Number_Systems.NUMBER_OF_PROBLEM_TYPES))
        elif problem_type == 1:
            self.problem_statement, self.ans = self.T1_Conversion()

    # problem type 1: Find the number after converting from one number system to another
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


# Contest 2 Topic 1: Prefix/Infix/Postfix Notation
class Prefix_Infix_PostFix_Notation(Problems):
    
    NUMBER_OF_PROBLEM_TYPES = 1

    def generate_problem(self, problem_type):
        if problem_type == 0:
            self.generate_problem(random.randint(1, Prefix_Infix_PostFix_Notation.NUMBER_OF_PROBLEM_TYPES))
        elif problem_type == 1:
            self.problem_statement, self.ans = self.T1_Conversion()
    
    def generate_notations(self):
        # add some weighted probability
        operators = ['+', '+', '+', '-', '-', '-', '*', '*', '/', '/', '^']
        
        num_operators = random.randint(7, 10)
        ops = [operators[random.randint(0, len(operators)-1)] for i in range(num_operators)]

        adj = [*([] for i in range(num_operators))]


        # TODO: use union find to randomly construct the edges 
        # num_operators-1 edges in the tree
        for i in range(num_operators-1):
            adj[i].append(i+1)
            adj[i+1].append(i)
        



        root = random.randint(0, num_operators-1)

        for i in range(num_operators):
            if i == root: 
                continue
            # add two numbers on the leaf operator node
            if len(adj[i]) == 1:
                # make number nodes negative to be distinguished from operator node
                adj[i].append(-random.randint(1, 9))

            adj[i].append(-random.randint(1, 9))

        prefix = []
        postfix = []

        def preorder(parent, cur):
            if cur < 0:
                prefix.append(-cur)
                return 
            else:
                prefix.append(ops[cur])

            for a in adj[cur]:
                if a != parent:
                    preorder(cur, a)

        preorder(-1, root)
        print(prefix)

        def postorder(parent, cur):
            if cur < 0:
                postfix.append(-cur)
                return 
            else:
                for a in adj[cur]:
                    if a != parent:
                        postorder(cur, a)

            postfix.append(ops[cur])

        postorder(-1, root)
        print(postfix)
        
        return prefix, postfix
                           

    # problem type 1: Translate the given notation into the other notation. Only involving prefix and postfix
    def T1_Translation(self):
        pass

    # problem type 2: Evaluate the given notation
    def T2_Evaluation(self):
        pass



p = Prefix_Infix_PostFix_Notation(1, 1)
p.generate_notations()