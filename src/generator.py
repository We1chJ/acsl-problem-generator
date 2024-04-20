"""
generator.py

the generator that takes in the requests info and calls functions to generate problems, decides which contest topic is queried.

"""
import random
import problems

NUMBER_OF_TOPICS = 1

def generate_1_problem(contest_topic, problem_type):

    if contest_topic == 0:
        return generate_1_problem(random.randint(1, NUMBER_OF_TOPICS), problem_type)

    elif contest_topic == 1:
        return problems.Computer_Number_Systems(contest_topic, problem_type)