#Entrada de Usuario
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome.strip() != '':
    print('Seu nome e:',nome)
    print('nome invertido e: {}'.format(nome[::-1]))
    #print('Seu nome contem (ou não) espaços:{}'format(ispace(nome)))#
    print('Seu nome tem {} Letras'.format(len(nome)))
    print('A primeira letra do seu nome e: {}'.format(nome[0]))
    print('A ultima letra do seu nome e:{}'.format(nome[-1]))
else:
    print('Desculpe você deixou campos vazios.')



