from random import randint

### Common Genetic Algorithm sequence:
# 1 - Create a population
# 2 - Fitness calculation
# 3 - Verify if found a solution
# 3.1 - Selection
# 3.2 - Crossover
# 3.3 - Mutation
# 4 - Solution found

### Base classes/functions
class Subject:
  def __init__(self, values:[int]):
    self.values = values

## Create a single subject node
def create_subject(subjects_size:int)->Subject:
  values = []

  for i in range(subjects_size):
    values.append(randint(0, 9))

  return Subject(values=values)

## Create a population based on chromosomes size
def create_population(chromosomes:int)->[Subject]:
  population = []

  for i in range(chromosomes):
    population.append(create_subject(subjects_size=6))

  return population

## Verifies the subject fitness value based on model
def fitness(subject:Subject)->int:
  fitness_value = 0

  for i in range(len(subject.values)):
    if (subject.values[i] == model[i]):
      fitness_value += 1

  return fitness_value

### Selection
def selection(population:[Subject]):
  scored = []
  selected = []
  parents = 2

  scored = [(fitness(subject=subject), subject.values) for subject in population]
  scored = [fitness_value_with_subject for fitness_value_with_subject in sorted(scored)]

  for i in range(len(scored)):
    print(scored[i], '\n')

  selected = scored[(len(scored) - parents):]

  return selected, scored

def crossover(selected, scored):
  print('crossover')

def mutation():
  print('mutation')

if __name__ == '__main__':
  model = [1, 2, 3, 4, 5, 6]
  chromosomes=80
  population = create_population(chromosomes=chromosomes)

  # for i in range(chromosomes):
  selected, scored = selection(population=population)
