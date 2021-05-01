from random import randint, sample

### Common Genetic Algorithm sequence:
# 1 - Create a population
# 2 - Fitness calculation
# 3 - Verify if found a solution
# 3.1 - Selection
# 3.2 - Crossover
# 3.3 - Mutation
# 4 - Solution found

### Base constants/functions
PARENTS: int = 2
SUBJECT_SIZE: int = 6

## Create a single subject node
def create_subject(subject_size:int=SUBJECT_SIZE)->[int]:
  values = []

  for i in range(subject_size):
    values.append(randint(0, 9))

  return values

## Create a population based on chromosomes size
def create_population(chromosomes:int)->[[int]]:
  population = []

  for i in range(chromosomes):
    population.append(create_subject())

  return population

## Verifies the subject fitness value based on model
def fitness(subject:[int])->int:
  fitness_value = 0

  for i in range(len(subject)):
    if (subject[i] == model[i]):
      fitness_value += 1

  return fitness_value

### Selection strategy: selects the two most fit
def selection(population:[int]):
  scored_subjects = []
  selected = []

  scored_subjects = [(fitness(subject=subject), subject) for subject in population]
  scored_subjects = [fitness_value_with_subject[1] for fitness_value_with_subject in sorted(scored_subjects)]

  selected = scored_subjects[len(scored_subjects) - PARENTS:]

  return crossover(selected=selected, population=scored_subjects)

def crossover(selected:[[int]], population:[[int]]):
  for i in range(len(population) - PARENTS):
    point = randint(1, SUBJECT_SIZE - 1)
    parent = sample(population=selected, k=2)

    population[i][:point] = parent[0][:point]
    population[i][point:] = parent[1][point:]

  return population

def mutation():
  print('mutation')

if __name__ == '__main__':
  model = [1, 2, 3, 4, 5, 6]
  chromosomes = 80
  population = create_population(chromosomes=chromosomes)

  # for i in range(chromosomes):
  population = selection(population=population)
