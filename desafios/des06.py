nome = input('Digite seu nome: ')
tamanho_nome= len(nome)

if tamanho_nome > 1:
    if tamanho_nome <=4:
        print('Seu nome e muito curto')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome e do tamanho normal')
    else:
        print('Seu nome e muito grande')
else:
    print('Digite mais de uma letra') 