from random import choice, randint, random, sample
from string import ascii_letters

MODEL = input('Type a model: ')
INDIVIDUAL_SIZE = len(MODEL)
NUMBER_OF_PARENTS = 2
MUTATION_PROB = 0.5
CHROMOSOMES = 100

# Create a individual node
def create_individual(individual_size:int)->str:
  individual = ''

  for _ in range(individual_size):
    individual += choice(ascii_letters)

  return individual

# Create a population based on chromosomes size
def create_population(chromosomes:int)->[str]:
  population = []

  for _ in range(chromosomes):
    population.append(create_individual(individual_size=INDIVIDUAL_SIZE))

  return population

# Verifies the individual fitness value based on containing individual chars
def fitness(individual:str)->int:
  fitness_value = 0

  for individual_char in range(len(individual)):
    fitness_value += abs(ord(individual[individual_char]) - ord(MODEL[individual_char]))

  return fitness_value

# Selects the two most fit (smallest score == most fit)
def selection(population:[str])->[[str], [str]]:
  scored_individuals = [(fitness(individual), individual) for individual in population]
  scored_individuals = [scored_individual[1] for scored_individual in sorted(scored_individuals)]

  most_fit = scored_individuals[:NUMBER_OF_PARENTS]

  return [most_fit, scored_individuals]

def crossover(selected:[str], population:[str])->[str]:
  for i in range(len(population)):
    shuffled_parents = sample(selected, len(selected))
    crossover_index = randint(0, INDIVIDUAL_SIZE - 1)

    mutable_individual = list(population[i])

    mutable_individual[:crossover_index] = shuffled_parents[0][:crossover_index]
    mutable_individual[crossover_index:] = shuffled_parents[1][crossover_index:]

    population[i] = ''.join(mutable_individual)

  return population

def mutation(population:[str])->[str]:
  for i in range(len(population) - NUMBER_OF_PARENTS):
    if (random() <= MUTATION_PROB):
      mutable_individual = list(population[i])

      index_for_mutation_value = randint(0, INDIVIDUAL_SIZE - 1)
      new_value = choice(ascii_letters)

      while new_value == mutable_individual[index_for_mutation_value]:
        new_value = choice(ascii_letters)

      mutable_individual[index_for_mutation_value] = new_value

      population[i] = ''.join(mutable_individual)

  return population

if __name__ == '__main__':
  population = create_population(chromosomes=CHROMOSOMES)

  for i in range(CHROMOSOMES):\
    [selected, population] = selection(population)
    population = crossover(selected, population)
    population = mutation(population)

  print(selected, population)

