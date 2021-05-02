from random import choice, randint, random, sample
from string import ascii_letters

### Genetic Algorithm sequence:
# 1 - Create a population
# 2 - Fitness calculation
# 3 - Verify if found a solution
# 3.1 - Selection
# 3.2 - Crossover
# 3.3 - Mutation
# 4 - Solution found

### Base constants/functions
MODEL = 'victor'
SUBJECT_SIZE = len(MODEL)
NUMBER_OF_PARENTS = 2
MUTATION_PROB = 0.5
CHROMOSOMES = 80

## Create a single subject node
def create_subject(subject_size:int=SUBJECT_SIZE)->str:
  subject = ''

  for _ in range(subject_size):
    subject += choice(ascii_letters)

  return subject

## Create a population based on chromosomes size
def create_population(chromosomes:int)->[str]:
  population = []

  for i in range(chromosomes):
    population.append(create_subject())

  return population
