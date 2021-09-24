sub_total = input('Ingrese el monto a pagar: ')
total = None
if sub_total.isnumeric():
    sub_total = float(sub_total)
    if sub_total >= 0:
        if sub_total < 800:
            pass
        elif sub_total < 1500:
            total = sub_total *(1 - 0.1)
        elif sub_total < 5000:
            total = sub_total *(1 - 0.15)
        else:
            total = sub_total *(1 - 0.2)
    else:
        print('Sub total debe ser positivo')
    
    print(f'Debe pagar {total} luego de su descuento')    
else:
    print(f'El valor {total} no es numerico')        
        