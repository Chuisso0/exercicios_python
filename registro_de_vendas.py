import os
from time import sleep



produtos = {'batata': 14.99, 'cebola': 13.50, 'alface': 2, 'pera': 15.40}
vendas = {}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear' )


# ------------------------------ cadastrar_produtos -------------------------

def cadastrar_produtos():

    while True:      
        limpar_tela()
        print('-- Realizando Cadastro de Produto --')

        produto = input('Qual o nome do produto? \n')

        if produto == '':

            while True:
                cancelar = input('Valor não reconhecido, deseja cadastrar algum produto? [S/N]').strip().upper()[0]

                if cancelar == 'S':
                    break

                elif cancelar == 'N':
                    return
                
                else: 
                    continue
            continue
        

        try:
            preco = float(input('Quanto custa? \n'))

        except ValueError: 
            print('Valor digitado inválido')
            continue
        produtos[produto] = preco


        while True:
            continuar = input('Continuar? [S/N]').strip().upper()[0]

            if continuar == 'S':
                break

            elif continuar == 'N':
                return
            
            else:
                print('nao entendi, quer registrar mais produtos? [S/N]')
                continue
        continue



# ------------------------------ realizar_vendas -------------------------

def realizar_venda():
    while True:
        limpar_tela()

        print('-- produtos disponíveis --')

        for produto, preco in produtos.items():
            print(f'{produto} - R${preco:.2f}')

        produto_desejado = input('escreva o nome do produto desejado: ')

        if produto_desejado == '':
            while True:
                continuar = input('Valor não reconhecido, realizar alguma venda? [S/N]').strip().upper()[0]

                if continuar == 'S':
                    break

                elif continuar == 'N':
                    return
                
                else:
                    continue
            continue
        

        if produto_desejado in list(produtos.keys()):

            try:
                quantidade = int(input('Quantos deseja?'))
                total_do_produto = produtos[produto_desejado] * quantidade
                vendas[produto_desejado] = quantidade, total_do_produto

            except ValueError:
                print('Valor inválido, refaça por favor')
                sleep(2)
                continue

            while True:
                continuar = input('Quer comprar mais alguma coisa? \n').upper().strip()[0]

                if continuar == 'S':
                    break

                elif continuar == 'N':
                    return
                
                else:
                    continue
            continue



# ------------------------------ Relatorio de vendas -------------------------

def relatorio_vendas():
    limpar_tela()
    print('-- Relatório de vendas --')

    if not vendas:
        print('Nenhuma venda realizada.')

    for produto, venda in vendas.items():
        print(f'produto: {produto}, qnt: {venda[0]}, total: {venda[1]:.2f}')


cadastrar_produtos()
realizar_venda()
relatorio_vendas()