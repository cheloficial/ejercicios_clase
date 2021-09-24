temperature = 90
t_unit = 'F'

if (t_unit == 'f') or (t_unit == 'F'):
    t_celsius = round((temperature - 32) * (5/9), 2)
    print(f'La temperatura es {t_celsius}°C')

elif (t_unit == 'k') or (t_unit == 'K'):
    t_celsius = round(temperature - 273.15, 2)
    print(f'La temperatura es {t_celsius}°C')