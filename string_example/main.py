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

  # Selects the two most fit (smallest score == most fit)
  def selection(population:[str])->[[str], [str]]:
    scored_individuals = [(fitness(individual), individual) for individual in population]
    scored_individuals = [scored_individual[1] for scored_individual in sorted(scored_individuals)]

    most_fit = scored_individuals[:NUMBER_OF_PARENTS]

    return [most_fit, scored_individuals]

  population = create_population(chromosomes=CHROMOSOMES)

  # for i in range(CHROMOSOMES):
  [selected, population] = selection(population=population)

  print(selected, population)


