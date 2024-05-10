import random
import time

class GeneticAlgorithm:
    def __init__(self, num_questions, pop_size, crossover_prob, mutation_prob, max_generations):
        self.num_questions = num_questions
        self.pop_size = pop_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.max_generations = max_generations
        self.population = []

    def initialize_population(self):
        for _ in range(self.pop_size):
            individual = [random.choice([0, 1]) for _ in range(self.num_questions)]
            self.population.append(individual)

    def fitness(self, individual):
        return sum(individual)

    def selection(self):
        total_fitness = sum(self.fitness(individual) for individual in self.population)
        probabilities = [self.fitness(individual) / float(total_fitness) for individual in self.population]
        selected = random.choices(self.population, probabilities, k=2)
        return selected

    def crossover(self, parent1, parent2):
        crossover_points = sorted(random.sample(range(1, self.num_questions), 2))
        child1 = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] + parent1[crossover_points[1]:]
        child2 = parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]] + parent2[crossover_points[1]:]
        return child1, child2

    def mutation(self, individual):
        mutated_individual = individual[:]
        for i in range(len(mutated_individual)):
            if random.random() < self.mutation_prob:
                mutated_individual[i] = 1 - mutated_individual[i]
        return mutated_individual

    def evolve(self):
        new_population = []

        for _ in range(self.pop_size // 2):
            parent1, parent2 = self.selection()
            if random.random() < self.crossover_prob:
                child1, child2 = self.crossover(parent1, parent2)
            else:
                child1, child2 = parent1[:], parent2[:]
            child1 = self.mutation(child1)
            child2 = self.mutation(child2)
            new_population.extend([child1, child2])

        self.population = new_population

    def get_best_solution(self):
        return max(self.population, key=self.fitness)

def main():
    num_questions = 10
    pop_size = 15
    crossover_prob = 0.6
    mutation_prob = 0.5
    max_generations = 30

    genetic_algo = GeneticAlgorithm(num_questions, pop_size, crossover_prob, mutation_prob, max_generations)
    genetic_algo.initialize_population()

    start_time = time.time()
    for generation in range(max_generations):
        genetic_algo.evolve()
        best_solution = genetic_algo.get_best_solution()
        print("Generation {}: Best solution = {}, Fitness = {}".format(generation + 1, best_solution, genetic_algo.fitness(best_solution)))

    end_time = time.time()
    computational_time = end_time - start_time
    print("Computational Time: {:.4f} seconds".format(computational_time))

if __name__ == "__main__":
    main()