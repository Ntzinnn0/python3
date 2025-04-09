"""
 Exercício
 Peça ao usuário para digitar seu nome
 Peça ao usuário para digitar sua idade
 Se nome e idade forem digitados:
     Exiba:
         Seu nome é {nome}
         Seu nome invertido é {nome invertido}
         Seu nome contém (ou não) espaços
         Seu nome tem {n} letras
         A primeira letra do seu nome é {letra}
         A última letra do seu nome é {letra}
 Se nada for digitado em nome ou idade: 
     exiba "Desculpe, você deixou campos vazios."
 """

#Entrada de Usuario
nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome.strip() != '': #verificaçao que algo foi digitado#
    print('Seu nome e:',nome)
    print('nome invertido e: {}'.format(nome[::-1]))
    print('Seu nome tem {} Letras'.format(len(nome)))
    print('A primeira letra do seu nome e: {}'.format(nome[0]))
    print('A ultima letra do seu nome e:{}'.format(nome[-1]))
else:
    print('Desculpe você deixou campos vazios.')

if ' ' in nome: #verificaçao de espaço na str#
    print("seu nome contem (ou não) espaços:'sim'")
else:
    print("seu nome contem (ou não) espaços:'Não'")

