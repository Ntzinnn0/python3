#Entrada de Usuario
nome = input('Digite seu nome:')
idade = input('Digite sua idade: ')
#funçoes:
funcao1= ('Seu nome e:{}'.format(nome))
funcao2= ('Seu nome invertido e:'(nome[::-1]))
funcao3= ('Seu nome contem (ou não) espaços:')

if nome.strip() != '':
 print(funcao1)
 print(funcao2)
 print(funcao3)
else:
    print('error')

