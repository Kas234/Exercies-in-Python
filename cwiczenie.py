# slownik

from random import choice
capitals = {
    'Poland': 'Warsaw',
    'France': 'Paris',
    'Germany': 'Berlin'
}

selected_country = choice(list(capitals.keys()))

capital = input(f'What is the capital of: {selected_country}? ')

if capitals[selected_country] == capital:
    print('Zgadza się')
else:
    print('Niestety nie! Chodziło o ', capitals[selected_country])



