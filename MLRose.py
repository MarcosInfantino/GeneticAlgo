from commons import product_prices
from commons import product_spaces
from config import CONFIG
from commons import products
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def fitness_function(chromosome):
    score = 0
    sum_spaces = 0
    for gen_index in range(len(chromosome)):
        if chromosome[gen_index] == 1:
            score += product_prices[gen_index]
            sum_spaces += product_spaces[gen_index]
    if sum_spaces > CONFIG.SPACE_LIMIT:
        score = 1
    return score


fitness = mlrose.CustomFitness(fitness_function)

problem = mlrose.DiscreteOpt(length=len(products), fitness_fn=fitness, maximize=True, max_val=2)  # 0, 1

best_solution, best_fitness = mlrose.genetic_alg(problem, pop_size=20, mutation_prob=0.01)

print(','.join(str(item) for item in best_solution))
print(fitness_function(best_solution))
for i in range(len(best_solution)):
    if best_solution[i] == 1:
        print('Name: ', products[i].name, ' - Price: ', products[i].price)
