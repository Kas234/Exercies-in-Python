def say_hello(first_name=''):
    print(f'Witaj {first_name}!')

say_hello('Ala')
say_hello('Witek')
say_hello()


def calculate_brutto(netto, vat=0.23):
    return netto + netto * vat

total = calculate_brutto(100)
total += calculate_brutto(200)
print(total)