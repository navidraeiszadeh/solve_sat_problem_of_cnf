import sys
# from SATSolver import SATSolver
import numpy as np
import random
from itertools import product
import math
import pysat
from pysat.formula import CNF
from pysat.solvers import Solver

cnf = CNF('Input.cnf')
max = 100     # must be completed
temperature = len(cnf.clauses)
size = len(cnf.clauses)
random_cnf = np.random.choice([0, 1], cnf.nv)  # it makes zero and one as a count of variable to make a first example

def convert_to_cnf(cnf_valuation):  #convert binary cnf to a literal list
    literals = []
    for i in range(len(cnf_valuation)):
        if cnf_valuation[i] == 1:
            literals.append(i + 1)
        else:
            literals.append(-(i + 1))
    return literals

def count_satisfying_assignments(cnf):
    global size
    num_vars = size  #calculate the number of variable of cnf
    num_satisfying = 0
    for assignment in product([-1, 1], repeat=num_vars):  # it build a cartesian product 
        #  generates all possible combinations of variable assignments for the num_vars variables. Each combination is represented by an assignment
        satisfiable = True  
        for clause in num_vars:
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

def possibility(E1, E2):
    global temperature
    delta_f = math.fabs(E1 - E2)
    result = math.exp(-delta_f / temperature)
    return result

def add_noise_possibility(cnf_value , num):
    new_cnf_valuation = cnf_value                # add a noise
    variable = random.randint(0, num)     #cnf.nv -> total variable count
    new_cnf_valuation[variable] = '0' if new_cnf_valuation[variable] == '1' else '1'
    # new_cnf_valuation = new_cnf_valuation[:variable] + temp + new_cnf_valuation[variable+1:]
    return new_cnf_valuation

def simulated_annealing(random_cnf_example): #implement algorithem
    print (random_cnf_example)
    global cnf
    for i in range(max):  
        temp_random_deep_copy = random_cnf_example.copy()
        cnf_with_noise = add_noise_possibility(temp_random_deep_copy , cnf.nv - 1)    
        first_energic = count_satisfying_assignments(random_cnf_example)    #fitness for finding energic       
        second_energic = count_satisfying_assignments(cnf_with_noise)
        if first_energic < second_energic:
            random_cnf_example = cnf_with_noise
            continue
        
        tmp = possibility(first_energic, second_energic) #find possibility with annealing formula
        
        if random.random() <= tmp:
            random_cnf_example = cnf_with_noise
            print(f'new value {second_energic}, i : {i}, t : {temperature}, p:{tmp}')
            
        # check the end conditions:
        if count_satisfying_assignments(random_cnf_example) == len(cnf.clauses):
            break
        
    print(f'valuation : {convert_to_cnf(random_cnf_example)}\nwith fitness value : {count_satisfying_assignments(random_cnf_example)}')   
    
simulated_annealing(random_cnf)    