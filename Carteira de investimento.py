print('\033[1;32m               Carteira de Investimento\033[m')
renda_fixa = dict()
ações = dict()
fiis = dict()
exterior = dict()
cont = 0
print('-=' * 30)
print('[1] Renda fixa;'
'\n[2] Ações;'
'\n[3] Fundos imobiliários;'
'\n[4] Investimento no exterior;'
'\n[0] Encerrar programa.')
escolha = int(input('Digite a opção: '))
print('-=' * 30)
while escolha == 1:
    cont += 1
    renda_fixa['Investimento'] = str(input('Nome do investimento: '))
    renda_fixa['Valor'] = float(input('Valor: '))
    print('Investimento adicionado com sucesso.')
    print('-=' * 30)
    print('[1] Renda fixa;'
    '\n[2] Ações;'
    '\n[3] Fundos imobiliários;'
    '\n[4] Investimento no exterior;'
    '\n[0] Encerrar programa.')
    escolha = int(input('Digite a opção: '))
print(renda_fixa)
    
