import random
import math
import time

N = 8 
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.1
ELITE_PERCENT = 0.1  
CROSSOVER_POINTS = 2


Min_Initial_Temp = float(input("Enter the Min Temp: "))
Max_Initial_Temp = float(input("Enter the Max Temp: "))

Min_Rate = float(input("Enter the minimum Rate of Cooling :"))
Max_Rate = float(input("Enter the maximum Rate of Cooling :"))

INITIAL_TEMPERATURE_RANGE = (Min_Initial_Temp, Max_Initial_Temp)
COOLING_RATE_RANGE = (Min_Rate, Max_Rate)

def fitness(board):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return 1 / (conflicts + 1) 

def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = [random.randint(0, N - 1) for _ in range(N)]
        population.append(individual)
    return population

def crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(1, N), CROSSOVER_POINTS))
    child = [-1] * N
    for i in range(crossover_points[0]):
        child[i] = parent1[i]
    for i in range(crossover_points[0], crossover_points[1]):
        child[i] = parent2[i]
    for i in range(crossover_points[1], N):
        child[i] = parent1[i]
    return child

def mutate(individual):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(N), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

def genetic_algorithm():
    population = initialize_population()

    for generation in range(NUM_GENERATIONS):
        population = sorted(population, key=lambda x: fitness(x), reverse=True)

        elite_count = int(ELITE_PERCENT * POPULATION_SIZE)
        next_generation = population[:elite_count]

        for _ in range(POPULATION_SIZE - elite_count):
            parent1, parent2 = random.choices(population, k=2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)

        population = next_generation

        if fitness(population[0]) == 1:
            break

    return population[0]

def neighbor_solution(current_solution):
    new_solution = current_solution[:]
    idx1, idx2 = random.sample(range(N), 2)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

def acceptance_probability(old_fitness, new_fitness, temperature):
    if new_fitness > old_fitness:
        return 1
    return math.exp((new_fitness - old_fitness) / temperature)

def simulated_annealing():
    current_solution = random.sample(range(N), N)
    current_fitness = fitness(current_solution)

    initial_temperature = random.uniform(*INITIAL_TEMPERATURE_RANGE)
    cooling_rate = random.uniform(*COOLING_RATE_RANGE)
    temperature = initial_temperature

    while temperature > 1e-3:
        new_solution = neighbor_solution(current_solution)
        new_fitness = fitness(new_solution)

        if new_fitness > current_fitness:
            current_solution = new_solution
            current_fitness = new_fitness
        else:
            if random.random() < acceptance_probability(current_fitness, new_fitness, temperature):
                current_solution = new_solution
                current_fitness = new_fitness

        temperature *= 1 - cooling_rate

    return current_solution

start_time_ga = time.time()
solution_ga = genetic_algorithm()
end_time_ga = time.time()

print("Solution found by Genetic Algorithm:", solution_ga)
print("Time taken by Genetic Algorithm:", end_time_ga - start_time_ga, "seconds")

start_time_sa = time.time()
solution_sa = simulated_annealing()
end_time_sa = time.time()

print("Solution found by Simulated Annealing:", solution_sa)
print("Time taken by Simulated Annealing:", end_time_sa - start_time_sa, "seconds")
5