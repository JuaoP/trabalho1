count = 0
resp = str(input('Telefonou para a vítima?'))
if resp == 'sim' or resp == 's':
    count = count + 1

resp = str(input('Esteve no local do crime?'))
if resp == 'sim' or resp == 's':
    count = count + 1

resp = str(input('Mora perto da vítima?'))
if resp == 'sim' or resp == 's':
    count = count + 1

resp = str(input('Devia para a vítima?'))
if resp == 'sim' or resp == 's':
    count = count + 1

resp = str(input('Já trabalhou com a vítima?'))

if resp == 'sim' or resp == 's':
    count = count + 1

if count == 2:
    print('Suspeita')

elif count == 3 or count == 4:
    print('Cúmplice')

elif count == 5:
    print('Assassino')

else:
    print('Inocente')
