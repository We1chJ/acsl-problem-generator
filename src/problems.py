"""
problems.py

Contains all the information and functions for each problems
"""

import random
import re

class Problems:
    def __init__(self, contest_topic, problem_type):
        self.contest_topic = contest_topic
        self.problem_type = problem_type
        self.problem_statement = None
        self.ans = None
        self.check_ans = None

    def generate_problem(self):
        pass

    def default_check_ans(self, response):
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
            self.problem_statement, self.ans, self.check_ans = self.T1_Conversion()

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

        return statement, ans, self.default_check_ans


# Contest 2 Topic 1: Prefix/Infix/Postfix Notation
class Prefix_Infix_PostFix_Notation(Problems):
    
    NUMBER_OF_PROBLEM_TYPES = 2

    def generate_problem(self, problem_type):
        if problem_type == 0:
            self.generate_problem(random.randint(1, Prefix_Infix_PostFix_Notation.NUMBER_OF_PROBLEM_TYPES))
        elif problem_type == 1:
            self.problem_statement, self.ans, self.check_ans = self.T1_Translation()
        elif problem_type == 2:
            self.problem_statement, self.ans, self.check_ans = self.T2_Evaluation()
    
    def generate_notations(self):
        # add some weighted probability
        operators = ['+', '+', '+', '-', '-', '-', '*', '*', '/', '/', '^']
        
        num_operators = random.randint(6, 9)
        ops = random.sample(operators, k=num_operators)

        adj = [*([] for i in range(num_operators))]

        ind = [i for i in range(num_operators)]
        # union find data structures
        father = [i for i in range(num_operators)]
        def find(a):
            if father[a] == a:
                return father[a]
            father[a] = find(father[a])
            return father[a]

        def unite(a, b):
            ra = find(a)
            rb = find(b)
            father[ra] = rb

        # TODO: use union find to randomly construct the edges
        # num_operators-1 edges in the tree
        for i in range(num_operators-1):
            a = random.choice(ind)
            b = random.choice(ind)
            while find(a) == find(b):
                b = random.choice(ind)
            
            adj[a].append(b)
            adj[b].append(a)
            
            unite(a, b)

            # make sure out degrees is <= 2, in degree can be at most 1
            if len(adj[a]) == 3:
                ind.remove(a)
            
            if len(adj[b]) == 3:
                ind.remove(b)

        root = random.choice(ind)

        # append numbers on the leaf nodes
        for i in range(num_operators):
            if i == root:
                if len(adj[i]) == 1:
                    adj[i].append(-random.randint(1, 9))
            elif len(adj[i]) == 2:
                # add one number on the leaf operator node
                # make number nodes negative to be distinguished from operator node
                adj[i].append(-random.randint(1, 9))
            elif len(adj[i]) == 1:
                # add two numbers
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
        
        return prefix, postfix

    def evaluate_prefix(self, input):
        print(input)
        print(re.findall("[^\+\-\*\/\^123456789]", str(input)))

        pass
        

    # problem type 1: Translate the given notation into the other notation. Only involving prefix and postfix
    def T1_Translation(self):
        prefix, postfix = self.generate_notations()
        r = random.random()

        if r < 0.5:
           # prefix -> postfix
           statement = "Given the following expression in Prefix Notation, rewrite it in Postfix Notation. Assume all numbers are single digits: \n" + ''.join(str(x) for x in prefix)
           ans = ''.join(str(x) for x in postfix)
           return statement, ans, self.default_check_ans
        else:
            # postfix -> prefix
            statement = "Given the following expression in Postfix Notation, rewrite it in Prefix Notation. Assume all numbers are single digits: \n" + ''.join(str(x) for x in postfix)
            ans = ''.join(str(x) for x in prefix)
            return statement, ans, self.default_check_ans

    # problem type 2: Evaluate the given notation
    def T2_Evaluation(self):
        prefix, postfix = self.generate_notations()
        r = random.random()

        self.evaluate_prefix(''.join(str(x) for x in prefix))

        if r < 0.5:
           # prefix
           statement = "Evaluate the following Prefix Notation. Assume all numbers are single digits: \n" + ''.join(str(x) for x in prefix)
           
        

           return statement, ans
        else:
            # postfix
            statement = "Evaluate the following Postfix Notation. Assume all numbers are single digits: \n" + ''.join(str(x) for x in postfix)
            ans = ''.join(str(x) for x in prefix)
            return statement, ans
        

p = Prefix_Infix_PostFix_Notation(2, 2)
prefix, postfix = p.generate_notations()
p.evaluate_prefix(''.join(str(x) for x in prefix))