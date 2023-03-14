from gaFromScratch import execute_ga_from_scratch
from gaWithMLRose import execute_ga_mlrose
from config import CONFIG

NUMBER_OF_RUNS = 100

ga_from_scratch_results_sum = 0
ga_with_mlrose_results_sum = 0

for i in range(NUMBER_OF_RUNS):
    ga_from_scratch_results_sum += execute_ga_from_scratch()
    ga_with_mlrose_results_sum += execute_ga_mlrose()

print("----------------------------------------------------------------------------------")
print("COMPARISON RESULTS")
print("----------------------------------------------------------------------------------")
print("GENERAL CONFIG VALUES")
print("NUMBER OF RUNS: ", NUMBER_OF_RUNS)
print("SPACE LIMIT: ", CONFIG.SPACE_LIMIT)
print("POPULATION SIZE: ", CONFIG.POPULATION_SIZE)
print("MUTATION PROBABILITY: ", CONFIG.MUTATION_PROBABILITY)
print("----------------------------------------------------------------------------------")
print("GA FROM SCRATCH CONFIG VALUES")
print("GENERATIONAL LEAP: ", CONFIG.GENERATIONAL_LEAP)
print("NUMBER OF GENERATIONS: ", CONFIG.NUMBER_OF_GENERATIONS)
print("CROSSOVER FUNCTION: ", CONFIG.CROSSOVER_FUNCTION)
print("SELECTION FUNCTION: ", CONFIG.SELECTION_FUNCTION)
print("----------------------------------------------------------------------------------")
print("RESULTS: ")
print("\t GA FROM SCRATCH AVERAGE RESULT: ", ga_from_scratch_results_sum/NUMBER_OF_RUNS)
print("\t GA WITH MLROSE AVERAGE RESULT: ", ga_with_mlrose_results_sum/NUMBER_OF_RUNS)

