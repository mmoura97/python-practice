# Exercicio - folha_pagamento

nome = input('Qual o Nome do Funcionario? \n')
cargo = int(input('Qual o cargo do Funcionario com numeros? (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário) \n'))
salarioBase = float(input('Qual o salario do Funcionario? \n'))
horasExTrabalhadas = int(input('Quantas horas extras ele trabalhou? \n'))
faltasNoMes = int(input('Quantas faltas ele teve no mes? \n'))
recebeuBonus = input('O funcionario rtecebeu algum bonus? (sim ou não) \n')

he = (salarioBase * 0.015) * horasExTrabalhadas
descontofaltas =  (salarioBase * 0.02) * faltasNoMes
valorbonus = 0

if recebeuBonus.lower() == 'sim':
  if cargo == 1:
    valorbonus = 1000
  elif cargo == 2:
    valorbonus = 500
  elif cargo == 3:
    valorbonus = 300
  elif cargo == 4:
    valorbonus = 100
  else:
    print('Não encontrado')
else:
  print('Não recebeu bonus')

totalDeAcrescimos = he + valorbonus
totalDeDescontos = descontofaltas

print('--- Folha de Pagemento ---')
print(f'O funcionario {nome}')
print('------')
print(f'O seu salario bruto é de R$ {salarioBase:.2f}')
print('------')
print(f'O seu total de Acresimos é de R$ {totalDeAcrescimos:.2f}')
print('------')
print(f'O seu total de Descontos é de R$ {totalDeDescontos:.2f}')
print('------')
print(f'O seu salario liquido é de R$ {salarioBase + totalDeAcrescimos - totalDeDescontos:.2f}')