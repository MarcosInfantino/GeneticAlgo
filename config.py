class Config:
    def __init__(self):
        self.SPACE_LIMIT = 5
        self.POPULATION_SIZE = 100
        self.GENERATIONAL_LEAP = 0.7
        self.NUMBER_OF_GENERATIONS = 200
        self.MUTATION_PROBABILITY = 0.1
        # CROSSOVER_FUNCTION VALUES:
        #   "RANDOM": cruza binomial aleatoria
        #   "SINGLE_POINT": cruza simple
        #   "MASK": cruza binomial con máscara doble
        RANDOM = "RANDOM"
        SINGLE_POINT = "SINGLE_POINT"
        MASK = "MASK"
        self.CROSSOVER_FUNCTION = RANDOM
        # MASKS
        self.MASK_FIRST_CHILD = "XXYYXYXXXYYYXYXYYYXX"
        self.MASK_SECOND_CHILD = "YYXXYXYYYXXXYXYXXXYY"
        #SELECTION FUNCTION
        TOURNAMENT = "TOURNAMENT"
        ROULETTE = "ROULETTE"
        self.SELECTION_FUNCTION = TOURNAMENT


CONFIG = Config()
