import random

# Parameters
POP = 10
N = 8
SELECT = 3
MR = 0.1
CR = 0.8
GEN = 5

# Parking slots and distance from entrance
slots = ['A','B','C','D','E','F','G','H']
distance = [2,5,3,7,4,6,8,9]


# Fitness
def fitness(ch):
    total = 0
    for i in range(N):
        if ch[i] == 1:
            total += distance[i]

    if sum(ch) != SELECT:
        return 0

    # Smaller distance = better fitness
    return 1 / (1 + total)


# Create initial population
def create_population():
    pop = []
    for i in range(POP):
        ch = [0] * N
        pos = random.sample(range(N), SELECT)
        for j in pos:
            ch[j] = 1
        pop.append(ch)
    return pop


# Fix chromosome to select exactly 3 slots
def fix(ch):
    while sum(ch) > SELECT:
        i = random.choice([i for i in range(N) if ch[i] == 1])
        ch[i] = 0

    while sum(ch) < SELECT:
        i = random.choice([i for i in range(N) if ch[i] == 0])
        ch[i] = 1
    return ch


# Selection
def select(pop):
    p1 = random.choice(pop)
    p2 = random.choice(pop)
    return p1 if fitness(p1) > fitness(p2) else p2


# Crossover
def cross(p1, p2):
    if random.random() < CR:
        point = random.randint(1, N-1)
        c1 = p1[:point] + p2[point:]
        c2 = p2[:point] + p1[point:]
        return fix(c1), fix(c2)
    return p1[:], p2[:]


# Mutation
def mutate(ch):
    for i in range(N):
        if random.random() < MR:
            ch[i] = 1 - ch[i]
    return fix(ch)


# Genetic Algorithm
def ga():
    pop = create_population()
    best = None
    best_fit = -1

    for generation in range(GEN):
        # Find best chromosome
        for ch in pop:
            f = fitness(ch)
            if f > best_fit:
                best_fit = f
                best = ch[:]

        # Calculate actual total distance for logging
        current_distance = sum(distance[i] for i in range(N) if best[i] == 1)
        
        # FIXED: Printing Total Distance as an integer instead of a decimal
        print(f"Generation {generation + 1}: Best Total Distance = {current_distance}")

        # New population
        new_pop = []
        while len(new_pop) < POP:
            p1 = select(pop)
            p2 = select(pop)

            c1, c2 = cross(p1, p2)
            c1 = mutate(c1)
            c2 = mutate(c2)

            new_pop.append(c1)
            if len(new_pop) < POP:
                new_pop.append(c2)

        pop = new_pop

    return best, best_fit


# Run GA
best, best_fit = ga()

# Output
print("\n========== FINAL RESULT ==========")
print("Best Parking Arrangement:", best)

print("Selected Slots: ", end="")
for i in range(N):
    if best[i] == 1:
        print(slots[i], end=" ")

total_distance = sum(distance[i] for i in range(N) if best[i] == 1)
print("\nMinimum Total Distance:", total_distance)
