import random

# -----------------------------------------
# 1. Define the problem
# -----------------------------------------

employees = ["A", "B", "C", "D", "E"]

skill = [8, 7, 9, 6, 10]


def fitness(chromosome):
    # Must select exactly 3 employees
    

    total_skill = 0

    for i in range(len(chromosome)):

        if chromosome[i] == 1:
            total_skill += skill[i]

    return total_skill


# -----------------------------------------
# 2. Initialize parameters
# -----------------------------------------

POPULATION_SIZE = 10
CHROMOSOME_LENGTH = 5
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.8
GENERATIONS = 5


# -----------------------------------------
# 3. Create initial population
# -----------------------------------------

def create_population():

    return [
        [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]
        for _ in range(POPULATION_SIZE)
    ]


# -----------------------------------------
# 4. Selection
# -----------------------------------------

def selection(population):

    parent1 = random.choice(population)
    parent2 = random.choice(population)

    if fitness(parent1) > fitness(parent2):
        return parent1
    else:
        return parent2


# -----------------------------------------
# 5. Crossover
# -----------------------------------------

def crossover(parent1, parent2):

    if random.random() < CROSSOVER_RATE:

        point = random.randint(1, CHROMOSOME_LENGTH - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    return parent1[:], parent2[:]


# -----------------------------------------
# 6. Mutation
# -----------------------------------------

def mutation(chromosome):

    for i in range(CHROMOSOME_LENGTH):

        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]

    return chromosome


# -----------------------------------------
# 7. Genetic Algorithm
# -----------------------------------------

def genetic_algorithm():

    population = create_population()

    best_solution = None
    best_fitness = float("-inf")

    for generation in range(GENERATIONS):

        # Evaluate fitness
        for individual in population:

            current_fitness = fitness(individual)

            if current_fitness > best_fitness:

                best_fitness = current_fitness
                best_solution = individual[:]


        print(
            f"Generation {generation + 1}: "
            f"Best = {best_solution}, "
            f"Fitness = {best_fitness}"
        )


        # Create new population
        new_population = []

        while len(new_population) < POPULATION_SIZE:

            # Selection
            parent1 = selection(population)
            parent2 = selection(population)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        population = new_population


    # -----------------------------------------
    # 8. Final result
    # -----------------------------------------

    print("\n========== FINAL RESULT ==========")

    print("Best chromosome:", best_solution)
    print("Maximum skill:", best_fitness)

    print("Selected Employees:")

    for i in range(CHROMOSOME_LENGTH):

        if best_solution[i] == 1:
            print(employees[i])


# -----------------------------------------
# Run the Genetic Algorithm
# -----------------------------------------

genetic_algorithm()