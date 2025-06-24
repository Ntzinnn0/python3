digita_hora = input('Digite o horario')

hora = int(digita_hora)

try:
    if hora > 0 and hora < 11:
        print ('Bom dia')
    elif hora > 11 and hora < 17:
        print('Boa tarde')
    else:

except: