
print('='*50)
print('Olá , Bem vindo ao nosso conversor de temperatura hhehe')
print('De qual escala deseja converter? \n'
'( K ) - Kelvin \n'
'( C ) - Celsius \n'
'( F ) - Fahrenheit')
print('='*50)

while True:

    escala1 = input('Digite a escala: \n').strip()[0].upper()

    if escala1 == 'K' or escala1 == 'C' or escala1 == 'F':
        break

    else:
        print(f'[ERRO], apenas K, C, ou F aceito,letra digitada é invalida')
        True

graus = float(input('Quantos graus? \n '))

while True:

    escala2 = input('Digite a escala: \n').strip()[0].upper()

    if escala2 == 'K' or escala2 == 'C' or escala2 == 'F':
        break

    else:
        print(f'[ERRO], apenas K, C, ou F aceito,letra digitada é invalida')
        True


if escala1 == 'K':

    if escala2 == 'C':
        print(f'{graus}°{escala1}, é equivalente a {graus - 273}°{escala2}')

    elif escala2 == 'F':
        print(f'{graus}°{escala1}, é equivalente a {(graus - 273) * 1.8 + 32}°{escala2}')


if escala1 == 'C':

    if escala2 == 'K':
        print(f'{graus}°{escala1}, é equivalente a {graus + 273}°{escala2}')

    if escala2 == 'F':
        print(f'{graus}°{escala1}, é equivalente a {graus * 1.8 + 32}°{escala2}')


if escala1 == 'F':

    if escala2 == 'C':
        print(f'{graus}°{escala1}, é equivalente a {(graus - 32) / 1.8}°{escala2}')

    if escala2 == 'K':
        print(f'{graus}°{escala1}, é equivalente a {(graus - 32) * 5/9 + 273}°{escala2}')       