"""
Server.py

Acting as the server. Either will be the web application or the discord server bot

Handles I/O, receives from the client, and sends out requests to generator, check answers, score keeping etc.
"""

import generator

contest_topic = int(input("Contest Topic: "))
if contest_topic == 0:
    problem_type = 0
else:
    problem_type = int(input("Problem Type ID: "))

problem = generator.generate_1_problem(contest_topic, problem_type)
problem.generate_problem(problem_type)
print(problem.problem_statement)

# Answer key for reference
print("Answer key for reference: ", problem.ans)
response = input("Your answer: ")
print(problem.check_ans(response))