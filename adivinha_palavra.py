import os

palavra_secreta = 'sabonete'
numero_tentativas = 0
letra_secreta = ''

os.system('cls')

while True:
    letra_user = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_user) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_user in palavra_secreta:
        letra_secreta += letra_user

    palavra_correta = ''

    for letra in palavra_secreta:
        
        if letra in letra_secreta:
            palavra_correta += letra

        else:
            palavra_correta += '*'
    print(palavra_correta)
    
    if palavra_correta == palavra_secreta:
        os.system('cls')
        print(f'GANHOU!!! PARABENS!!')
        print(f'A palavra era: {palavra_correta}')
        print(f'Numero de tentativas: {numero_tentativas}')
        break
