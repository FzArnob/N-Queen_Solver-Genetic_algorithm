import random
import sys


def random_chromosome(size):
    return [random.randint(1, nq) for _ in range(nq)]


def fitness(chromosome):
    horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2

    n = len(chromosome)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return int(maxFitness - (horizontal_collisions + diagonal_collisions))


def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness


def random_population(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Error"


def crossover(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]


def mutation(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x


def genetic_algo(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_population(population, probabilities)
        y = random_population(population, probabilities)
        child = crossover(x, y)
        if random.random() < mutation_probability:
            child = mutation(child)
        new_population.append(child)
        if fitness(child) == maxFitness:
            break
    return new_population


if __name__ == "__main__":
    nq = int(input("Enter Number of Queens: "))
    maxFitness = (nq * (nq - 1)) / 2  # 8*7/2 = 28
    population = [random_chromosome(nq) for _ in range(10)]
    print()
    print("Dimension : ", nq, "X", nq, "\nPopulation : ", len(population), "\n")
    max_generation = int(input("Enter Maximun Generation Count: "))
    print()
    generation = 1
    solve = 0
    while not maxFitness in [fitness(chrom) for chrom in population]:
        # generations
        population = genetic_algo(population, fitness)
        percent = 100.0 * generation / max_generation
        sys.stdout.write('\r')
        sys.stdout.write("Generation : [{:{}}] {:>3}% > Count: {:>3}".format('=' * int(percent / (100.0 / 50)),
                                                                             50, int(percent), generation))
        sys.stdout.flush()

        generation += 1
        if generation > max_generation:
            solve = -1
            break
    print("\n")
    if solve == -1:
        print("No Solution found in ", max_generation, "Generations!")
    else:
        chrom_out = []
        for chrom in population:
            if fitness(chrom) == maxFitness:
                print("Solution : ", chrom)
                chrom_out = chrom

        board = []
        for x in range(nq):
            board.append(["⬜"] * nq)
        for i in range(nq):
            board[nq - chrom_out[i]][i] = "⬛"


        def print_board(board):
            for row in board:
                print(" ".join(row))


        print("\nSolution Board:")
        print_board(board)
