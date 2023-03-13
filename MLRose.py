from commons import product_prices
from commons import product_spaces
from config import CONFIG
from commons import products
import six
import sys

sys.modules['sklearn.externals.six'] = six
import mlrose


# Se define la función fitness de una forma similar al caso anterior
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


fitness = mlrose.CustomFitness(
    fitness_function)  # Se genera una función fitness de MLRose a partir de la nuestra personalizada

problem = mlrose.DiscreteOpt(length=len(products), fitness_fn=fitness, maximize=True, max_val=2)  # 0, 1
# DiscreteOpt -> Para problemas de optimización con números enteros (los parámetros del array solución solo pueden ser números enteros)
# length -> Cantidad de parámetros a modificar para la optimización (longitud del array solución)
# fitness_fn -> función fitness
# maximize -> para elegir si queremos resolver un problema de maximización o minimización
# max_val -> los componentes del array solución solo pueden tomar valores menores a max_val (en este caso binarios, 0 y 1)

best_solution, best_fitness = mlrose.genetic_alg(problem, pop_size=CONFIG.POPULATION_SIZE,
                                                 mutation_prob=CONFIG.MUTATION_PROBABILITY)

print(','.join(str(item_flag) for item_flag in best_solution))
print("Best individual score: ", str(best_fitness))

for i in range(len(best_solution)):
    if best_solution[i] == 1:
        print('Name: ', products[i].name, ' - Price: ', products[i].price)
