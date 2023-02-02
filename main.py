from random import random
import plotly.express as px

# CONFIGURACION
MUTATION_RATE = 0.01
SPACE_LIMIT = 5
POPULATION_SIZE = 100
GENERATIONAL_LEAP = 0.7
NUMBER_OF_GENERATIONS = 200
MUTATION_PROBABILITY = 0.1


# -------------------------

class Product:
    def __init__(self, name, space, price):
        self.name = name
        self.space = space
        self.price = price


products = [Product('Refrigerator A', 0.751, 999.90), Product('Cell phone', 0.00000899, 2199.12),
            Product('TV 55', 0.400, 4346.99), Product("TV 50' ", 0.290, 3999.90), Product("TV 42' ", 0.200, 2999.00),
            Product("Notebook A", 0.00350, 2499.90), Product("Ventilator", 0.496, 199.90),
            Product("Microwave A", 0.0424, 308.66), Product("Microwave B", 0.0544, 429.90),
            Product("Microwave C", 0.0319, 299.29), Product("Refrigerator B", 0.635, 849.00),
            Product("Refrigerator C", 0.870, 1199.89), Product("Notebook B", 0.498, 1999.90),
            Product("Notebook C", 0.527, 3999.00), Product("Notebook D", 0.597, 2999.00),
            Product("Notebook E", 0.300, 1999.00), Product("Notebook F", 0.127, 999.00),
            Product("Notebook G", 0.27, 99.00), Product("Cell C", 0.97, 199.00)]

product_prices = []
for prod in products:
    product_prices.append(prod.price)
product_spaces = []
for prod in products:
    product_spaces.append(prod.space)

print(product_prices)


class Individual:
    def __init__(self, chromosome=[]):
        if not chromosome:
            self.chromosome = []
            for i in range(len(product_prices)):
                if random() < 0.5:
                    self.chromosome.append(0)
                else:
                    self.chromosome.append(1)
        else:
            self.chromosome = chromosome

    def fitness(self):
        score = 0
        sum_spaces = 0
        for gen_index in range(len(self.chromosome)):
            if self.chromosome[gen_index] == 1:
                score += product_prices[gen_index]
                sum_spaces += product_spaces[gen_index]
        if sum_spaces > SPACE_LIMIT:
            score = 1
        return score

    def print(self):
        print(self.chromosome)


def get_initial_population():
    _population = []
    for i in range(POPULATION_SIZE):
        _population.append(Individual())
    return _population


def total_sum_fitness_function(_population):
    _sum = 0
    for ind in _population:
        _sum += ind.fitness()
    return _sum


def select_individual_by_roulette(_population, fitness_function_sum):
    _random = random() * fitness_function_sum
    _sum = 0
    _index = 0
    while _index < len(_population):
        _sum += _population[_index].fitness()
        if _sum >= _random:
            return _population[_index]
        else:
            _index += 1


def get_population_after_selection(old_population):
    new_population = []
    fitness_function_sum = total_sum_fitness_function(old_population)
    for individual_index in range(len(old_population)):
        new_population.append(select_individual_by_roulette(old_population, fitness_function_sum))
    return new_population


def single_point_crossover(individual1, individual2):
    cutoff = round(random() * len(individual1.chromosome))
    chromosome1 = individual1.chromosome[0:cutoff] + individual2.chromosome[cutoff::]
    chromosome2 = individual2.chromosome[0:cutoff] + individual1.chromosome[cutoff::]
    child1 = Individual(chromosome1)
    child2 = Individual(chromosome2)
    return [child1, child2]


def get_population_after_crossover(old_population):
    gen_leap_length = round((len(old_population) * GENERATIONAL_LEAP) / 2 - 0.1) * 2
    parents = old_population[0:gen_leap_length]
    crossed_population = []
    for pi in range(0, len(parents), 2):
        children = single_point_crossover(old_population[pi], old_population[pi + 1])
        crossed_population.append(children[0])
        crossed_population.append(children[1])
    return crossed_population + old_population[gen_leap_length::]


def get_best_individual(_population):
    best_fitness = -1
    best_ind = 0
    for ind in _population:
        current_fitness = ind.fitness()
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_ind = ind
    return best_ind


def get_mutation_position(_population):
    return round(random() * len(_population) * len(_population[0].chromosome))


def get_population_after_mutation(_population):
    mutation_probability = random()
    if mutation_probability <= MUTATION_PROBABILITY:
        mutation_pos = len(_population)

        while mutation_pos == len(_population):
            mutation_pos = get_mutation_position(_population)

        individual_index = mutation_pos // len(_population)
        chromosome_index = mutation_pos % len(_population[0].chromosome)

        if _population[individual_index].chromosome[chromosome_index] == 0:
            _population[individual_index].chromosome[chromosome_index] = 1
        else:
            _population[individual_index].chromosome[chromosome_index] = 0

    return _population


# ALGORITMO
# ---------GENERACIÓN DE LA POBLACIÓN INCIAL

population = get_initial_population()
solutions = []
for gen_number in range(NUMBER_OF_GENERATIONS):
    population = get_population_after_selection(population)
    population = get_population_after_crossover(population)
    population = get_population_after_mutation(population)
    print("Best individual of generation " + str(gen_number + 1) + " : ")
    print(len(population))
    best = get_best_individual(population)
    best.print()
    solutions.append(best.fitness())
    print("Fitness function value: " + str(best.fitness()))

figure = px.line(x=range(0, NUMBER_OF_GENERATIONS), y=solutions, title='Genetic algorithm results')
figure.show()
