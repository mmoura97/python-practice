#Exercicio - dias_para_idade

## usando a // descartamos as casas decimais e retornamos apenas interiros diferente da / que retorna casas decimais e precisamos formatar com o format
print('Coversor de dias em Idade')
print()
idadeEmDias = int(input('Digite a sua idade em dias: '))
anos2 = idadeEmDias / 365
meses2 = (idadeEmDias % 365) / 30
dias2 = (idadeEmDias % 365) / 30
print()
print(f'Voce tem {anos2:.0f} anos e {meses2:.0f} meses e {dias2:.0f} dias')

