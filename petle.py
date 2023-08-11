# for - wykonuje się skończoną ilość  razy (ilość elementów, range())

for n in range(10):
    print(n)

for m in range(5):
    print('Cześć')

# while - wykonuje się dopóki twierdzenie jest prawdziwe

number_of_entries = 0
while number_of_entries < 30:
    entries = int(input('Ile osób wchodzi? '))
    number_of_entries += entries

    print('Razem osób: ', number_of_entries)