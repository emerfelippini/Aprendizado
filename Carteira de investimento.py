print('\033[1;32m               Carteira de Investimento\033[m')
renda_fixa = dict()
lista_rf = list()
fundo_imobiliario = dict()
lista_fiis = list()
exterior = dict()
lista_exterior = list()
ações = dict()
lista_ações = list()
soma_carteira_total = 0
print('-=' * 30)
print('[1] Renda fixa;'
'\n[2] Ações;'
'\n[3] Fundos imobiliários;'
'\n[4] Investimento no exterior;'
'\n[0] Encerrar programa.')
escolha = int(input('Digite a opção: '))
print('-=' * 30)
while escolha == 1:
    renda_fixa.clear()
    renda_fixa['Investimento'] = str(input('Nome do investimento: '))
    renda_fixa['Valor'] = float(input('Valor: '))
    soma_carteira_total += renda_fixa['Valor']
    lista_rf.append(renda_fixa.copy())
    print('Investimento adicionado com sucesso.')
    print('-=' * 30)
    print('[1] Renda fixa;'
    '\n[2] Ações;'
    '\n[3] Fundos imobiliários;'
    '\n[4] Investimento no exterior;'
    '\n[0] Encerrar programa.')
    escolha = int(input('Digite a opção: '))
while escolha == 3:
    fundo_imobiliario.clear()
    fundo_imobiliario['Investimento'] = str(input('Nome do investimento: '))
    fundo_imobiliario['Valor'] = float(input('Valor: '))
    soma_carteira_total += fundo_imobiliario['Valor']
    lista_fiis.append(fundo_imobiliario.copy())
    print('Investimento adicionado com sucesso.')
    print('-=' * 30)
    print('[1] Renda fixa;'
    '\n[2] Ações;'
    '\n[3] Fundos imobiliários;'
    '\n[4] Investimento no exterior;'
    '\n[0] Encerrar programa.')
    escolha = int(input('Digite a opção: '))
while escolha == 2:
    ações.clear()
    ações['Investimento'] = str(input('Nome do investimento: '))
    ações['Valor'] = float(input('Valor: '))
    soma_carteira_total += ações['Valor']
    lista_ações.append(ações.copy())
    print('Investimento adicionado com sucesso.')
    print('-=' * 30)
    print('[1] Renda fixa;'
    '\n[2] Ações;'
    '\n[3] Fundos imobiliários;'
    '\n[4] Investimento no exterior;'
    '\n[0] Encerrar programa.')
    escolha = int(input('Digite a opção: '))
while escolha == 4:
    exterior.clear()
    exterior['Investimento'] = str(input('Nome do investimento: '))
    exterior['Valor'] = float(input('Valor: '))
    soma_carteira_total += exterior['Valor']
    lista_exterior.append(exterior.copy())
    print('Investimento adicionado com sucesso.')
    print('-=' * 30)
    print('[1] Renda fixa;'
    '\n[2] Ações;'
    '\n[3] Fundos imobiliários;'
    '\n[4] Investimento no exterior;'
    '\n[0] Encerrar programa.')
    escolha = int(input('Digite a opção: '))
if escolha == 0:
    print('Finalizando programa.')
while escolha > 4:
    print('Escolha inválida.')
    print('[1] Renda fixa;'
    '\n[2] Ações;'
    '\n[3] Fundos imobiliários;'
    '\n[4] Investimento no exterior;'
    '\n[0] Encerrar programa.')
    escolha = int(input('Digite a opção: '))
print('-=' * 40)
print(f'Sua carteira tem R$ {soma_carteira_total:.2f}')
for cont in lista_rf:
    print(f'Foram registrados {len(lista_rf)} investimentos em renda fixa, no valor de: {sum(lista_rf[cont][1])}')
