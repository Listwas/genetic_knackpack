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

def copy_individual(ind):
    return ind[:]

# --- init population ---
population = random_population()
fitness_values = fitnesses(population)

# --- find best individual in first population ---
best_idx = fitness_values.index(max(fitness_values))
best_individual = copy_individual(population[best_idx])
best_fitness = fitness_values[best_idx]

print("=== Genetic Algorithm for Knapsack ===")
print(f"Items: {NUMBER_OF_GENES}, Capacity: {capacity}")
print(f"Population size: {POPULATION_SIZE}, Generations: {GENERATIONS}")
print(f"Initial best fitness: {best_fitness}")
print("-" * 50)

# --- main evolution loop ---
for generation in range(1, GENERATIONS + 1):
    new_population = []

    while len(new_population) < POPULATION_SIZE:
        parent1 = roulette_selection(population, fitness_values)
        parent2 = roulette_selection(population, fitness_values)

        child1, child2 = one_point_crossover(parent1, parent2)

        child1 = mutate(child1)
        child2 = mutate(child2)

        new_population.append(child1)
        if len(new_population) < POPULATION_SIZE:
            new_population.append(child2)

    population = new_population
    fitness_values = fitnesses(population)

    # --- Elitism keep the best individual so far ---
    current_best_fitness = max(fitness_values)
    if current_best_fitness > best_fitness:
        best_idx = fitness_values.index(current_best_fitness)
        best_individual = copy_individual(population[best_idx])
        best_fitness = current_best_fitness

    # --- replace worst with best (stronger elitism) ---
    worst_idx = fitness_values.index(min(fitness_values))
    if best_fitness > fitness_values[worst_idx]:
        population[worst_idx] = copy_individual(best_individual)
        fitness_values[worst_idx] = best_fitness

    print(f"Gen {generation:2d} | Best: {best_fitness}")
