first_name = input('Por favor ingrese su Nombre: ') 
last_name = input('Por favor ingrese su Apellido: ')
age = input('Por favor ingrese su edad: ')

print(f'Tu nombre tiene {len(first_name)} letras')
print(f'Tu apellido tiene {len(last_name)} letras')

if age.isnumeric():
    age = int(age)
    year_1 = 2021 - age
    year_2 = 2021 - (age + 1)
    print(f'Posibles años de nacimiento: {year_1}/{year_2}')

if len(first_name) > 6:
    print('Dude tu nombre tiene muchos caracteres')