from random import randint

### Common Genetic Algorithm sequence:
# 1 - Create a population
# 2 - Fitness calculation
# 3 - Verify if found a solution
# 3.1 - Selection
# 3.2 - Crossover
# 3.3 - Mutation
# 4 - Solution found

class Subject:
  def __init__(self, values:[int]):
    self.values = values

### Base functions
def create_subject(subjects_size:int):
  values = []

  for i in range(subjects_size):
    values.append(randint(0, 9))

  return Subject(values=values)

def create_population(chromosomes:int)->[Subject]:
  population = []

  for i in range(chromosomes):
    population.append(create_subject(subjects_size=6))

  return population

def fitness():
  print('fitness')

### Selection strategy: random
def selection():
  print('selection')

def crossover():
  print('crossover')

def mutation():
  print('mutation')

if __name__ == "__main__":
  model = [1, 2, 3, 4, 5, 6]
  chromosomes=80

  population = create_population(chromosomes=chromosomes)

  for subject in population:
    print(subject.values)
