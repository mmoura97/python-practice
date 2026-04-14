#Exercicio - idade_em_dias

print('Bem vindo a calculadora de Idade em dias')
print()
ano = int(input('Digite quantos anos voce tem: '))
mes = int(input('Digite quantos meses voce tem:'))
dias = int(input('Digite quantos dias voce tem:'))

anosemdias = ano*365
mesEmDias = mes*30
idade = anosemdias + mesEmDias + dias
print()
print(f'A sua idade em dias é {idade}')
