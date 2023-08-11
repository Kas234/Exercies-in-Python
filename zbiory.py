first_name = set()

first_name.add('Michal')
first_name.add('Kacper')
first_name.add('Wojtek')
first_name.add('Kacper')

# można je dodawać, szukać częsci wspólnych/ różnych, różnice symetryczne

team_a = {'Wojtek', 'Adam', 'Michal'}
team_b = {'Wojtek', 'Adam', 'Karol', 'Kuba'}

print('Suma', team_a | team_b)
# nie powtarzają się
print('Część wspólna', team_a & team_b)
print('Różnica symetryczna', team_a ^ team_b)
print('A-B', team_a - team_b)
print('B-A', team_b - team_a)

