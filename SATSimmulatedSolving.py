import sys
from SATSolver import CnfResolver
import numpy as np
import random
import math


cnf = CnfResolver('Input.cnf')
max = 100     # must be completed
max_answer = cnf.clauses_size
temperature = cnf.clauses_size
noise_possibility = 0.1

def add_noise_possibility():
    d

def simulated_annealing(random_cnf_example):
    
    for i in range(max):  
        # temperature *= t_coefficient
        cnf_with_noise = add_noise_possibility(cnf_valuation=random_cnf_example.copy())    
        first_energic = fitness(random_cnf_example)    #fitness for finding energic       
        second_energic = fitness(random_cnf_example)
        if first_energic < second_energic:
            random_cnf_example = cnf_with_noise
            print(f'new value {fitness2}, i : {i}, t : {temperature}')
            continue
        rand_num = random.random()
        pos = possibility(fitness1, fitness2)
        if rand_num <= pos:
            random_cnf_example = temp_cnf_valuation
            print(f'new value {fitness2}, i : {i}, t : {temperature}, p:{pos}')
        # checking the end conditions:
        if fitness(random_cnf_example) == max_answer:
            break

    