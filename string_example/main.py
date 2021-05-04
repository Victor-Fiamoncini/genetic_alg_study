from random import choice, randint, random, sample
from string import ascii_letters

MODEL = 'victor'
INDIVIDUAL_SIZE = len(MODEL)
NUMBER_OF_PARENTS = 2
MUTATION_PROB = 0.5
CHROMOSOMES = 20

if __name__ == '__main__':
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

  # Selection strategy: selects the two most fit
  def selection(population:[str])->[str]:
    for individual in population:
      if individual == MODEL:
        print('Found')
        break

      individual_with_fitness_value = (individual, fitness(individual=individual))

      print('individual_with_fitness_value', individual_with_fitness_value, '\n')

  population = create_population(chromosomes=CHROMOSOMES)

  # for i in range(CHROMOSOMES):
  population = selection(population=population)


