from random import randint, random, sample

### Genetic Algorithm sequence:
# 1 - Create a population
# 2 - Fitness calculation
# 3 - Verify if found a solution
# 3.1 - Selection
# 3.2 - Crossover
# 3.3 - Mutation
# 4 - Solution found

### Base constants/functions
MODEL = [9, 9, 9, 9]
SUBJECT_SIZE = len(MODEL)
NUMBER_OF_PARENTS = 2
MUTATION_PROB = 0.5
CHROMOSOMES = 80

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
    if (subject[i] == MODEL[i]):
      fitness_value += 1

  return fitness_value

### Selection strategy: selects the two most fit
def selection(population:[int])->[[int]]:
  scored_subjects = []
  selected = []

  scored_subjects = [(fitness(subject=subject), subject) for subject in population]
  scored_subjects = [fitness_value_with_subject[1] for fitness_value_with_subject in sorted(scored_subjects)]

  selected = scored_subjects[len(scored_subjects) - NUMBER_OF_PARENTS:]

  return crossover(selected=selected, population=scored_subjects)

### Crossover strategy: selects two random point of a subject
def crossover(selected:[[int]], population:[[int]])->[[int]]:
  for i in range(len(population) - NUMBER_OF_PARENTS):
    point = randint(1, SUBJECT_SIZE - 1)
    parent = sample(population=selected, k=2)

    population[i][:point] = parent[0][:point]
    population[i][point:] = parent[1][point:]

  return population

### Mutation strategy: replace a subject random value/position with a new random value
def mutation(population:[[int]])->[[int]]:
  for i in range(len(population) - NUMBER_OF_PARENTS):
    if (random() <= MUTATION_PROB):
      index_for_mutation_value = randint(0, SUBJECT_SIZE - 1)
      new_value = randint(1, 9)

      while new_value == population[i][index_for_mutation_value]:
        new_value = randint(1, 9)

      population[i][index_for_mutation_value] = new_value

  return population

if __name__ == '__main__':
  population = create_population(chromosomes=CHROMOSOMES)

  print(f'Generation 1 - First Population: ', population, '\n')

  for i in range(CHROMOSOMES):
    population = selection(population=population)
    population = mutation(population=population)

  print(f'Generation {CHROMOSOMES} - Final Population: ', population, '\n')
