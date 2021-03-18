num = float(input('Digite um número: '))

if num == round(num):
    print("O número é inteiro!")
else:
    print("O número é decimal!")
    print("Arredondando para baixo: ", round(num - 0.5))
    print("Arredondando para cima: ", round(num + 0.5))
