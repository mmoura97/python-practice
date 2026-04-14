# Exercicio - emprestimo

nomecliente = input('Qual o seu nome? \n')
idade = int(input('Qual a sua Idade? \n'))
rendaMensal = float(input('Qual a sua Renda Mensal? \n'))
valorDesejado = int(input('Qual o valor do emprestimo que voce deseja? \n'))
parcelasDoEmprestimo = int(input('Quantas Parcelas voce deseja? \n'))

limite = rendaMensal * 15
valorParcela = valorDesejado / parcelasDoEmprestimo

if idade < 18:
  print('Emprestimo reprovado!')
  print('Motivo: por ser menor de idade')
elif valorDesejado > limite:
  print('Emprestimo reprovado!')
  print('Motivo: O valor do emprestimo é maior que sua renda mensal!')
elif parcelasDoEmprestimo < 3 or parcelasDoEmprestimo > 24:
  print('Emprestimo reprovado!')
  print('Motivo: A quantidade de parcelas não foi aceita!')
elif valorParcela < 100 or valorParcela >= 2000:
  print('Emprestimo reprovado!')
  print(f'Motivo: O valor da parcela R$ {valorParcela:.2f} não é aceito!')
else:
    juros = 0
    if parcelasDoEmprestimo <=6:
      juros = 0.05
    elif parcelasDoEmprestimo <=12:
      juros = 0.08
    else:
      juros = 0.10

    valor_total_com_juros = valorDesejado * (1 + juros * parcelasDoEmprestimo)
    valorDeCadaParcela = valor_total_com_juros / parcelasDoEmprestimo
    juros_totais_pagos = valor_total_com_juros - valorDesejado

    print('------')
    print('Resumo do seu Emprestimo:')
    print(f'\n--- Empréstimo APROVADO para {nomecliente}! ---')
    print(f'Valor Solicitado: R$ {valorDesejado:.2f}')
    print(f'Renda Mensal: R$ {rendaMensal:.2f}')
    print(f'Número de Parcelas: {parcelasDoEmprestimo}')
    print(f'Taxa de Juros Aplicada: {juros*100:.0f}%')
    print('--------------------------------------------------')
    print(f'Juros Totais Pagos: R$ {juros_totais_pagos:.2f}')
    print(f'Valor Total com Juros: R$ {valor_total_com_juros:.2f}')
    print(f'Valor de cada parcela: R$ {valorDeCadaParcela:.2f}')