import numpy as np
import random
import matplotlib.pyplot as plt
import pysat as py
import math
from pysat.formula import CNF

cnf = CNF('Input.cnf')
# number of current generation
number_of_generation = cnf.nv
# number of selected parent
number_of_selected_parent = 50 
mutation_percent = 0.8

class creature:
    def __init__(self, gene: list):
        self.gene = gene
        self.fitness = fitness(gene)     #calculate the fitness of that!

def fitness(cnf_test): #calculate the parantese count
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
    tempList = np.zeros(len(cnf.clauses))
    for i in range(cnf.nv):
        if cnf_test[i] == 1:
            contribution_set = contributions[i+1]
            for i in contribution_set:
                if tempList[i] == 0:
                    tempList[i] = 1
                    count_of_sat += 1
    return count_of_sat                    
            
def add_mution(cnf_value , num):
    new_cnf_valuation = cnf_value                # as like as noise
    variable = random.randint(0, num)     #cnf.nv -> total variable count
    new_cnf_valuation[variable] = '0' if new_cnf_valuation[variable] == '1' else '1'
    return new_cnf_valuation
                               
def choose_parent(generation_list):
    global number_of_generation
    best_member = int(number_of_selected_parent * 0.8)
    bottom_gen_num = number_of_selected_parent - best_member
    best_parent = [generation_list[i] for i in range((number_of_generation-best_member), number_of_generation)]
    parent_list2 = [generation_list[i] for i in range(0, bottom_gen_num)]
    return parent_list2.extend(best_parent)
            
def cross_over(P1 , P2):
    global cnf
    random_index = random.randint( 1 , cnf.nv)
    father_gene = [P1.gene[i] for i in range(random_index)]  # set it in a dictionory
    mother_gene = [P2.gene[i] for i in range(random_index, cnf.nv)]
    father_gene.extend(mother_gene)
    return add_mution(father_gene)   #cast it to creature??

first_cnf_example = [creature(np.random.choice([0, 1], size=cnf.nv)) for i in range(cnf.nv)] #make a first cnf
parent = []
new_generation = []

def genetic_algorithm(cnf, population_size, max_iterations, mutation_rate):
    for _ in range(max_iterations):     
        # Select parents 
        parents = choose_parent(first_cnf_example)
        # Perform crossover and mutation for create the next generation
        list = []
        for i in range(0, population_size, 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            child1 = cross_over(parent1, parent2)
            child2 = cross_over(parent2, parent1)
            mutated_child1 = add_mution(child1, mutation_rate)
            mutated_child2 = add_mution(child2, mutation_rate)
            list.extend([mutated_child1, mutated_child2])
        
        new_generation = list
    # Find the best solution from the final population
    best_solution = max(new_generation , key=lambda cnf_valuation: fitness(cnf_valuation, cnf))
    best_fitness = fitness(best_solution, cnf)
    print(f'BEST FITNESS = { best_fitness }')
    print(best_solution)
    return best_solution, best_fitness


for k in range(number_of_generation):
    print(f'cycle { k } with max value {first_cnf_example[-1].fitness}')
    first_cnf_example = genetic_algorithm(first_cnf_example , cnf.nv , len(cnf.clauses) , 0.8)
    if first_cnf_example[-1].fitness == len(cnf.clauses):
        break
