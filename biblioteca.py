import os


livros = {"1984": {
        'autor': 'George Orwell',
        'ano': 1949,
        'status': 'Emprestado'
    },
    "Dom Casmurro": {
        'autor': 'Machado de Assis',
        'ano': 1899,
        'status': 'Disponível'
    },
    "O Senhor dos Anéis": {
        'autor': 'J.R.R. Tolkien',
        'ano': 1954,
        'status': 'Emprestado'
    },
    "Cem Anos de Solidão": {
        'autor': 'Gabriel García Márquez',
        'ano': 1967,
        'status': 'Disponível'
    },
    'O Pequeno Príncipe': {
        'autor': 'Antoine de Saint-Exupéry',
        'ano': 1943,
        'status': 'Disponível'
    }}

# ------------------Adicionar-Livros--------------------

def adicionar_livro():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        adicionar = input('Deseja adicionar algum livro? [S/N] ').strip().upper()      

        if adicionar == 'S':
            titulo_livro = input('Escreva o titulo do livro: ')
            autor_livro = input('Autor do livro: ')

            try:
                ano_livro = int(input('Ano do livro: '))
                status_livro = int(input('status do livro: \nDisponivel[1] Emprestado[2]\n'))

            except ValueError:
                print('Valor nao reconhecido, preencha novamente')
                continue

            if status_livro == 1:
                status_livro = 'Disponivel'

            elif status_livro == 2:
                status_livro = 'Emprestado'

            else:
                print('status desconhecido, preencha apenas com [1] ou [2]')
                continue

            livros[titulo_livro] = {'autor' : autor_livro, 'ano' : ano_livro, 'status' : status_livro}

            analise_de_livros()

            print('Produto adicionado com sucesso!!')
            while True:
                adicionar_mais = input('quer adicionar mais? [S/N]').upper().strip()
                if adicionar_mais == 'S':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                if adicionar_mais == 'N':
                    return
                
                else: 
                    continue
            continue

        elif adicionar == 'N':
            return
        
        else:
            continue


livros_disponiveis = []
livros_emprestados = []

# ------------------Análise-de-Livros--------------------

def analise_de_livros():
    livros_emprestados.clear()
    livros_disponiveis.clear()
    for livro, info in livros.items():

        if info['status'] == 'Disponível':
            livros_disponiveis.append(livro)

        elif info['status'] == 'Emprestado':
            livros_emprestados.append(livro)

# ------------------Emprestar-Livros--------------------

def emprestar_livros():
    os.system('cls' if os.name == 'nt' else 'clear')
    analise_de_livros()
    print('-- Livros Disponíveis --')
    for n in range(0, len(livros_disponiveis)):
        print(f'{n} - {livros_disponiveis[n]}')

    try:
        livro_requerido = int(input('Qual livro deseja? Insira seu número. \n'))

        if not (0 <= livro_requerido < len(livros_disponiveis)):
            print('Livro não reconhecido')

        for n in range(0, len(livros_disponiveis)):

            if livro_requerido == n:
                livro_requerido = livros_disponiveis[n]

        for livro in livros.items():

            if list(livro)[0] == livro_requerido:
                livro[1]['status'] = 'Emprestado'

    except:
        print('Livro não reconhecido')

    analise_de_livros()

# ------------------Devolver-Livros--------------------

def devolver_livros():
    os.system('cls' if os.name == 'nt' else 'clear')
    analise_de_livros()
    print('-- Livros Emprestados --')
    for n in range(0, len(livros_emprestados)):
        print(f'{n} - {livros_emprestados[n]}')

    try:
        livro_devolvido = int(input('Qual livro devolver? Insira seu número. \n'))
        
        if not (0 <= livro_devolvido < len(livros_emprestados)):
            print('Livro não reconhecido.')
        

        for n in range(0, len(livros_emprestados)):

            if livro_devolvido == n:
                livro_devolvido = livros_emprestados[n]

        for livro in livros.items():

            if list(livro)[0] == livro_devolvido:
                livro[1]['status'] = 'Disponível'
    except:
        print('Livro não reconhecido.')

    analise_de_livros()


# ------------------Mostrar-Acervo--------------------
def mostrar_acervo():
    os.system('cls' if os.name == 'nt' else 'clear')
    for numero in livros.keys():
        print(numero)
        for n in list(livros[numero].items()):
            print(f'    {n[0]} : {n[1]}')
        
        

# ------------------Menu-Biblioteca--------------------


def menu_biblioteca():
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-- Biblioteca --')
        print('1 - Mostrar Acervo \n' \
            '2 - Adicionar Livro \n' \
            '3 - Emprestar Livro \n' \
            '4 - Devolver Livro \n' \
            '5- Sair')
        opcao = input('\nEscolha uma opção: \n')

        if opcao == '1':
            mostrar_acervo()
            input('\nAperte qualquer botão para retornar ao menu \n')
            

        elif opcao == '2':
            adicionar_livro()
            input('\nAperte qualquer botão para retornar ao menu \n')
        
        elif opcao == '3':
            emprestar_livros()
            input('\nAperte qualquer botão para retornar ao menu \n')

        elif opcao == '4':
            devolver_livros()
            input('\nAperte qualquer botão para retornar ao menu \n')

        elif opcao == '5':
            print('Até um outro dia..')
            break

        else:
            print('Opção inválida')
            continue


menu_biblioteca()
