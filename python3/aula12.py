#Exercício de programação com if e comparação
numero_1 = input('Degite um numero: ')
numero_2 = input('Digite outro numero: ')

#numero_1 = int(numero_1)
#numero_2 = int(numero_2)

if numero_1 > numero_2:
    print('O primeiro valor: {} ele e maior que o segundo Valor: {}'.format(numero_1, numero_2))
elif numero_2 > numero_1:
    print('O primeiro valor: {} ele e maior que o segundo Valor: {}'.format(numero_2, numero_1))
elif numero_1 == numero_2:
    print('O primeiro valor e o segundo valor são iguais.')
else:
    print('Nada aconteceu')

