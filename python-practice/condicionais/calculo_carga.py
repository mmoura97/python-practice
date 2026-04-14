#Exercicico - calculo_carga

# Aqui também temos uma forma de colocar esse elif (estado == 2 and codigo >= 21 and codigo <= 30):

estadosCarga = int(input('Qual o codigo do estado da Carga? (Digite entre 1 a 5)\n'))
pesoDaCarga = float(input('Qual o peso da carga em toneladas?\n'))
codigoDaCarga = int(input('Qual o código da carga? (Digite entre 10 a 40)\n'))

pesoEmQuilos = (pesoDaCarga * 1000)
precoPorKg = 0
valorDoImposto = 0


if codigoDaCarga >= 10 and codigoDaCarga <= 20:
  precoPorKg = 100
elif codigoDaCarga >= 21 and codigoDaCarga <=30:
  precoPorKg = 250
elif codigoDaCarga >= 31 and codigoDaCarga <=40:
  precoPorKg = 340
else:
  print('erro')

precoDaCarga  = pesoEmQuilos * precoPorKg

if estadosCarga == 1:
  valorDoImposto = 0.35 * precoDaCarga
elif estadosCarga == 2:
  valorDoImposto = 0.25 * precoDaCarga
elif estadosCarga == 3:
  valorDoImposto = 0.15 * precoDaCarga
elif estadosCarga == 4:
  valorDoImposto = 0.05 * precoDaCarga
elif estadosCarga == 5:
  valorDoImposto = 0.0 * precoDaCarga
else:
  print('erro')

ValorcargaTotal = precoDaCarga + valorDoImposto

print(f'O peso da sua carga em quilos é: {pesoEmQuilos}')
print(f'O preco da sua carga é R$ {precoDaCarga:.2f}')
print(f'O preco da seu imposto é R$ {valorDoImposto:.2f}')
print(f'O preco da carga com imposto é R$ {ValorcargaTotal:.2f}')