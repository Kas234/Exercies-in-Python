author = {
    'first_name' : 'Zofia',
    'last_name' : 'Nalkowska'
}

print(author['first_name'])
print(author['last_name'])

for item in author:
    print(item)

for item in author:
    print(item, author[item])

for item in author.items():
    print(item)

for item in author.items():
    print(item[0], item[1])

for first_name, last_name in author.items():
    print(first_name, last_name)