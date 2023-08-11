print('Hello World')
first_name = input('Jak masz na imię ')
print('Hello', first_name)

if first_name == 'Kasia':
    print('Hi Kasia')
else:
    print('Nie wiem kim jesteś, ale chętnie się dowiem')

age = input('Ile masz lat? ')

if int(age) >= 18:
    print('Jesteś pełnoletni ')
else:
    print('Musisz jeszcze poczekać ')
    wait_years = 18 - int(age)
    print('Będziesz dorosły za ', wait_years, 'lat.')



