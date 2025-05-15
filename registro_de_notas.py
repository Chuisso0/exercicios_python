import os

aluno = {} 


def cadastrar_aluno():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        nome = input('Qual o nome do aluno?\n')

        try:
            nota1 = float(input('Qual foi a primeira nota?\n'))
            nota2 = float(input('Qual foi a segunda nota?\n'))
            nota3 = float(input('Qual foi a terceira nota?\n'))

        except ValueError:
            print('Em notas, são aceitos apenas números. Por favor, refaça.')
            continue

        aluno[nome] = (nota1, nota2, nota3)
        
        while True:
            continuar = input('Quer continuar? [S/N] ')[0].strip().upper()

            if continuar == 'S':
                break

            elif continuar == 'N':
                return aluno
            
            else:
                print('Desculpa, não entendi. Apenas digite S ou N.')


def gerar_boletim():
    os.system('cls' if os.name == 'nt' else 'clear')

    for nome,nota in aluno.items():
        print(f'aluno: {nome} \n notas: {nota[0]}, {nota[1]}, {nota[2]} \n média: {(sum(nota)/len(nota)):.2f}')



cadastrar_aluno()
gerar_boletim()        