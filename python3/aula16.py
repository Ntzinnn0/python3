contador = input('Digite um numero: ')
contador = int(contador)


while contador <= 9:
    contador += 1

    if contador == 4:
        print('9')
        continue
    print(contador)

print('Acabou')


    