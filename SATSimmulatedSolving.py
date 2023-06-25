import sys
from SATSolver import CnfResolver
import numpy as np
import random
from itertools import product
import math


cnf = CnfResolver('Input.cnf')
max = 100     # must be completed
max_answer = cnf.clauses_size
temperature = cnf.clauses_size
noise_possibility = 0.1

def count_satisfying_assignments(cnf):
    num_vars = len(set(abs(literal) for clause in cnf for literal in clause))  #calculate the number of variable of cnf
    num_satisfying = 0
    
    for assignment in product([-1, 1], repeat=num_vars):  # it build a cartesian product 
        #  generates all possible combinations of variable assignments for the num_vars variables. Each combination is represented by an assignment
        satisfiable = True 
        
        for clause in cnf:
            clause_satisfying = False
            for literal in clause:
                var = abs(literal)   #the variable var stores the absolute value of the literal, representing the variable part.
                value = assignment[var-1]     #store the value of that -> is 1 or -1
                if (literal > 0 and value == 1) or (literal < 0 and value == -1):
                    clause_satisfying = True     #literal is satisfied
                    break
            
            if not clause_satisfying:
                satisfiable = False
                break
        
        if satisfiable:
            num_satisfying += 1
    
    return num_satisfying


def add_noise_possibility():
    d

def simulated_annealing(random_cnf_example):
    
    for i in range(max):  
        # temperature *= t_coefficient
        cnf_with_noise = add_noise_possibility(cnf_valuation=random_cnf_example.copy())    
        first_energic = count_satisfying_assignments(random_cnf_example)    #fitness for finding energic       
        second_energic = count_satisfying_assignments(random_cnf_example)
        if first_energic < second_energic:
            random_cnf_example = cnf_with_noise
            continue
        rand_num = random.random()
        pos = possibility(first_energic, second_energic)
        if rand_num <= pos:
            random_cnf_example = cnf_with_noise
            print(f'new value {second_energic}, i : {i}, t : {temperature}, p:{pos}')
        # checking the end conditions:
        if count_satisfying_assignments(random_cnf_example) == max_answer:
            break

    