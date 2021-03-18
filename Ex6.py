def calcular_precos():

    count = 0
    calculo_produto = 0


    dados_produto = [('Morango', 2.50, 2.20), ('Maçã', 1.80, 1.50)]

    while True:


        finalizar = False


        produto = input('Informe o produto desejado: (Morango ou Maçã):')

        for x in range(2):

            if produto == dados_produto[x][0]:

                count = x

                finalizar = True

                break

            else:
                if x == 1:

                    finalizar = False
                    print('Valor inválido, tente novamente.', produto)

        if finalizar:
            break

    while True:

        try:


            peso = float(input("Por favor, informe o peso desejado:"))


            if peso > 0:
                break

            else:
                continue

        except ValueError:
            print("Valor inválido do peso.")
            continue


    if peso <= 5 and peso > 0:

        calculo_produto = dados_produto[count][1] * peso

    elif peso > 5:

        calculo_produto = dados_produto[count][2] * peso

        if peso > 8 or calculo_produto > 25:
            calculo_produto = (dados_produto[count][2] * peso) - ((dados_produto[count][2] * peso) * 10 / 100)

    print("Valor a pagar:R$%.2f" % calculo_produto)


calcular_precos()