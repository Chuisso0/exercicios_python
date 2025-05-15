import random
import os
import time

def indecisao():
    os.system('cls')
    print('Olá, aqui vou te ajudar a tomar decisões')
    duvida = []
    while True:

        coisa = input('Digite aqui as opções: \n').upper().strip()
        if coisa == '':
            vazio = input('Vazio mesmo? [S][N]')
            if vazio[0] == 'S':
                print('Tudo bem')
            elif vazio[0] == 'N':
                print('beleza então, escolha o novo valor')
                coisa = input('Digite aqui: ')
        duvida.append(coisa)

        if len(duvida) >= 2:
            while True:
                continuar = input('Deseja continuar?[S][N] ').strip().upper()

                if continuar[0] == 'S':
                    break

                elif continuar[0] == 'N':
                    print('Tudo bem!')
                    time.sleep(0.5)
                    os.system('cls')
                    numeracao = random.randint(0, len(duvida)-1)
                    print(f'Entre as opções de: {duvida}')
                    time.sleep(0.5)
                    print(f'A sorteada foi : {duvida[numeracao]}')
                    return

                else:
                    print('[ERRO], Opção inválida')
                    continue

indecisao()

