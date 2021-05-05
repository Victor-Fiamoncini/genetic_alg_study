from random import randint, random, sample

MODEL = [9, 9, 9, 9]
SUBJECT_SIZE = len(MODEL)
NUMBER_OF_PARENTS = 2
MUTATION_PROB = 0.5
CHROMOSOMES = 80

if __name__ == '__main__':
  # Create a single subject node
  def create_subject(subject_size:int=SUBJECT_SIZE)->[int]:
    values = []

    for i in range(subject_size):
      values.append(randint(0, 9))

    return values

  # Create a population based on chromosomes size
  def create_population(chromosomes:int)->[[int]]:
    population = []

    for i in range(chromosomes):
      population.append(create_subject())

    return population

  # Verifies the subject fitness value based on model
  def fitness(subject:[int])->int:
    fitness_value = 0

    for i in range(len(subject)):
      if (subject[i] == MODEL[i]):
        fitness_value += 1

    return fitness_value

  # Selects the two most fit
  def selection(population:[int])->[[int]]:
    scored_subjects = []
    selected = []

    scored_subjects = [(fitness(subject=subject), subject) for subject in population]
    scored_subjects = [fitness_value_with_subject[1] for fitness_value_with_subject in sorted(scored_subjects)]

    selected = scored_subjects[len(scored_subjects) - NUMBER_OF_PARENTS:]

    return crossover(selected=selected, population=scored_subjects)

  # Crossover strategy: replace a subject value with some parent values
  def crossover(selected:[[int]], population:[[int]])->[[int]]:
    for i in range(len(population) - NUMBER_OF_PARENTS):
      index = randint(1, SUBJECT_SIZE - 1)
      parent = sample(population=selected, k=2)

      population[i][:index] = parent[0][:index]
      population[i][index:] = parent[1][index:]

    return population

  # Mutation strategy: replace a subject random value/position with a new random value
  def mutation(population:[[int]])->[[int]]:
    for i in range(len(population) - NUMBER_OF_PARENTS):
      if (random() <= MUTATION_PROB):
        index_for_mutation_value = randint(0, SUBJECT_SIZE - 1)
        new_value = randint(1, 9)

        while new_value == population[i][index_for_mutation_value]:
          new_value = randint(1, 9)

        population[i][index_for_mutation_value] = new_value

    return population

  population = create_population(chromosomes=CHROMOSOMES)

  print(f'Model {MODEL}', '\n')
  print(f'Generation 1 - First Population: ', population, '\n')

  for i in range(CHROMOSOMES):
    population = selection(population=population)
    population = mutation(population=population)

  print(f'Generation {CHROMOSOMES} - Final Population: ', population, '\n')
