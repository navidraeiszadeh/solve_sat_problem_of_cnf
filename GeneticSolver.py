import numpy as np
import random
import matplotlib.pyplot as plt
import pysat as py
import math
from pysat.formula import CNF


cnf = CNF('Input.cnf')
# number of current generation
mu = 2 * cn.nv
# number of selected parent
lmda = int(math.sqrt(mu)) #-> 80
mutation_percent = 0.95
top_membership_percent = 0.85
max_iteration = 10 * cn.clauses_size
max_answer = cn.clauses_size

class creature:
    def __init__(self, gene: list):
        self.gene = gene
        self.fitness = fitness(gene)     #calculate the fitness of that!


def fitness(cnf_test):
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
            


