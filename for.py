fruits= ['peach', 'orange', 'mango', 'lemon', 'lemon', 'apple']
fruits.sort()
for fruit in fruits:
    print(fruit)

vegetables = []
for i in range(5):
    vegetable = input(f'What is your {i+1} favourite vegetable: ')

trees = []
for i in range(5):
    trees.append(input(f'What is your {i+1} favourite tree: '))

trees.sort()
for tree in trees:
    print(tree)
