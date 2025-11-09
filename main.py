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

def fitnesses(population):
    return [fitness(individual) for individual in population]

def roulette_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        return random.choice(population)

    pick = random.uniform(0, total_fitness)
    current = 0

    for individual, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return individual

def one_point_crossover(parent1, parent2):
    point = random.randint(1, NUMBER_OF_GENES - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual):
    for i in range(NUMBER_OF_GENES):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

pop = random_population()
print("sample population fitnesses:", fitnesses(pop))
