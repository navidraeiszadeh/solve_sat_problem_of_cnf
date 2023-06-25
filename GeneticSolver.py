import numpy as np
import random
import matplotlib.pyplot as plt
import pysat as py
import math
from pysat.formula import CNF


cn = CnfResolver("input.cnf")
# number of current generation
mu = 2 * cn.nv
# number of selected parent
lmda = int(math.sqrt(mu)) #-> 80
mutation_percent = 0.95
top_membership_percent = 0.85
max_iteration = 10 * cn.clauses_size
max_answer = cn.clauses_size


# def fitness(cnf_valuation):
#     global cn

#     return cn.count_number_of_satisfactions(cnf_valuation)


class creature:
    def __init__(self, gene: list):
        self.gene = gene
        self.fitness = fitness(gene)     #calculate the fitness of that!

