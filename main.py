import random

weights = [2, 3, 5, 7, 9]
values  = [6, 5, 8, 9, 10]
capacity = 15

NUMBER_OF_GENES = len(weights)
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
GENERATIONS = 50


def random_individual():
    return [random.randint(0, 1) for _ in range(NUMBER_OF_GENES)]

def random_population():
    return [random_individual() for _ in range(POPULATION_SIZE)]

def fitness(individual):
    total_weight = 0
    total_value = 0

    for gene, w, v in zip(individual, weights, values):
        if gene == 1:
            total_weight += w
            total_value += v

    if total_weight > capacity:
        return 0

    return total_value

print(fitness(random_individual()))
