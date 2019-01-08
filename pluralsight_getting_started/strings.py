text = 'hello'

print(text.capitalize())

print(text.replace('e', 'a'))

print(text.isalpha())

print(text.isdigit())  # useful when converting to int

separated_text = "some, csv, values"
print(separated_text.split(','))

name = 'Luke'
machine = 'HAL'
print('Nice to meet you {0} I am {1}'.format(name, machine))
print(f'Nice to meet you {name} I am {machine}')
