
import os
os.system('cls')
lista = []
while True:

    opcao = input('Selecione uma opção: \n'
            '[i]nserir [a]pagar [l]istar\n')
    print('-=' * 10)
    if opcao == 'i':

        item = input('Digite algo para listar\n')
        lista.append(item)
        print('-=' * 10)
    if opcao == 'l':

        for coisas in enumerate(lista):
            print(coisas)
        print('-=' * 10)
    try:
        if opcao == 'a':
            apagar = int(input('Digite o indice que quer apagar:\n'))
            lista.pop(apagar)
            print('-=' * 10)
    except:
        print('Digite um dos indices da lista, pode verificar os indices com "l"')