temperature = input('Por favor ingrese la temperatura de la sala: ')
if temperature.isnumeric():
    
    temperature = float(temperature)
    t_unit = input('Por favor ingrese la unidad de la temperatura (K o F): ').upper()

    if t_unit == 'F':
        t_celsius = round((temperature - 32) * (5/9), 2)
    elif t_unit == 'K':
        t_celsius = round(temperature - 273.15, 2)
    else:
        print(f'La unidad {t_unit} no es valida')    
    if t_unit == 'K' or t_unit == 'F':
        print(f'La temperatura es {t_celsius}°C')

else:
    print(f'El valor {temperature} no es numerico')    