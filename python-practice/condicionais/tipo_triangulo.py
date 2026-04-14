# Exercicio - tipo_triangulo

A = float(input('Qual o valor do lado A do Trinangulo? \n'))
B = float(input('Qual o valor do lado B do Trinangulo? \n'))
C = float(input('Qual o valor do lado C do Trinangulo? \n'))

# ordenando para que sempre o maior numero seja a primeira posição e acessando cada um da lista para o if e else.
mariorLado = [A, B, C]
mariorLado.sort(reverse=True)
maiorA = mariorLado[0]
meioB = mariorLado[1]
menorC = mariorLado[2]

#if comparando os triangulos.
if maiorA >= meioB+menorC:
  print('Não é um tringulo ')
elif maiorA**2 == meioB**2 + menorC**2:
  print('É um trinagulo Retangulo')
elif maiorA**2 > meioB**2 + menorC**2:
  print('É um tringulo Obtusangulo')
elif maiorA**2 < meioB**2 + menorC**2:
  print('É um triangulo Acutangulo')
elif maiorA == meioB == menorC:
  print('É um triangulo Equilatero')
elif maiorA == meioB or maiorA == menorC or meioB == menorC:
  print('É um triangulo Isosceles')
else:
  print('estude geometria!!')
print(f'O maior lado do seu Tringulo é o A: {mariorLado[0]}')
print('Calculo Realizado!!')
