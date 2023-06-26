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
temperature = len(cnf.clauses) * 0.9  # 0.9 is alpha value to reduce tempretaure after per iteration
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

def count_satisfying_assignments(cnf_test):
    global cnf
    contributions = {}
    tmp = 0
    for clause in cnf.clauses:
        for literal in clause:
            if contributions.get(literal) is None:
                contributions[literal] = set()    
            contributions[literal].add(tmp)    
        tmp += 1
    count_of_sat = 0
    satisfied_parts = np.zeros(len(cnf.clauses))
    for i in range(cnf.nv):
        if cnf_test[i] == 1:
            contribution_set = contributions[i+1]
            for i in contribution_set:
                if satisfied_parts[i] == 0:
                    satisfied_parts[i] = 1
                    count_of_sat += 1
    return count_of_sat

def EnergicCheck(E1, E2):
    global temperature
    delta_f = math.fabs(E1 - E2)
    result = math.exp(-delta_f / temperature)
    return result

def add_noise_possibility(cnf_value , num):
    new_cnf_valuation = cnf_value                # add a noise  -> baz namaeei binary
    variable = random.randint(0, num)     #cnf.nv -> total variable number
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
        
        tmp = EnergicCheck(first_energic, second_energic) #find possibility with annealing formula
        
        if random.random() <= tmp:
            random_cnf_example = cnf_with_noise
            
        # check the end conditions:
        if count_satisfying_assignments(random_cnf_example) == len(cnf.clauses):
            break
    
    print(f' *** {convert_to_cnf(random_cnf_example)}  and value of energic is: {count_satisfying_assignments(random_cnf_example)}');    #for test  
    
simulated_annealing(random_cnf)    