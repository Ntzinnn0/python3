"""
 Faça um programa que peça ao usuário para digitar um número inteiro,
 informe se este número é par ou ímpar. Caso o usuário não digite um número
 inteiro, informe que não é um número inteiro.
 """
while True:
    digitar_numero = input('Digite um numero inteiro: ')
    if digitar_numero.lstrip('-').isdigit():
        break
    else:
        print('Por favor, digite um número ' \
        'inteiro válido (sem letras).')
    #if '.' in digitar_numero:
    #    print('Por favor, Digitar um numero inteiro')
    #else:
     #   break

digitar_numero= int(digitar_numero)

if digitar_numero % 2 == 0:
    print(f'O numero: {digitar_numero}, E um numero par')
else:
    print(f'O numero: {digitar_numero}, E um numero impar')


