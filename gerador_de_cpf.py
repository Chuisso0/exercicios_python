import os
import random

os.system('cls' if os.name == 'nt' else 'clear')

def gerador_de_cpf():
    print('-'*5,'TOME 10 CPFs VALIDOS', '-'*5)

    for i in range (10):

        cpf = ''
        for i in range(9):
            cpf += str(random.randint(0, 9))


        numero_calculado = 0
        multiplicador = 10

        for numero in cpf:
            numero_calculado += int(numero) * multiplicador
            multiplicador -= 1

        numero_calculado = (numero_calculado * 10) % 11

        primeiro_digito = numero_calculado if numero_calculado <= 9 else 0


        # 2) SEGUNDO DIGITO:

        cpf = f'{cpf}{primeiro_digito}'
        multiplicador = 11
        numero_calculado2 = 0

        for numero in cpf:

            numero_calculado2 += int(numero) * multiplicador
            multiplicador -= 1

        numero_calculado2 = (numero_calculado2 * 10) % 11

        segundo_digito = numero_calculado2 if numero_calculado2 <= 9 else 0


        # 3) CPF COMPLETO:

        cpf = f'{cpf}{segundo_digito}'
        print(f'      {"-"*4}{cpf}{"-"*4}')


gerador_de_cpf()