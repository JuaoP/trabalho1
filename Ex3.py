n1 = float(input('Informe o primeiro número:'))
n2 = float(input('Informe o segundo número:'))

print('Qual função você deseja realizar?')

funcao = int(input('Adição = 1 / Subtração = 2 / Divisão = 3 / Multiplicação = 4 : '))

if funcao == 1:
    resultado = n1 + n2
elif funcao == 2:
    resultado = n1 - n2
elif funcao == 3:
    resultado = n1 / n2
elif funcao == 4:
    resultado = n1 * n2
else:
    print('Opção inválida, tente novamente!')

print(f'O resultado é: {resultado}')

if resultado % 2 == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')

if resultado >= 0:
    print('O número é positivo!')
else:
    print('O número é negativo!')

if resultado % 1 == 0:
    print('O número é inteiro!')
else:
    print('O número é decimal!')


