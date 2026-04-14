# Exercicios - soma_impares

def obter_numero():
  while True:
    try:
      numero = int(input('Digite um numero \n'))
      if numero > 0:
        return numero
      else:
        print('Erro, numero invalido')
    except ValueError:
      print("Por favor, insira um número válido.")

n = obter_numero()
soma_de_impares = 0
contador_pares = 0
lista_de_impares = []
lista_pares_mult3 = []
i = 1
j = 1


while i <= n:
  if i % 2 != 0 and i <= n:
    lista_de_impares.append(i)
    soma_de_impares += i
  i += 1

for numero in range(1, n+1):
  if (numero % 2 == 0) and (numero % 3 == 0):
    contador_pares += 1
    lista_pares_mult3.append(numero)

print('Somando os numeros impares!')
print()
print(f'A lista de numeros impares é: {lista_de_impares}')
print(f'A soma dos numeros impares é: {soma_de_impares}')
print()
print('Somando os numeros pares!')
print()
print(f'A lista de numeros pares multiplicos de 3: {lista_pares_mult3}')
print(f'Quantidade de pares múltiplos de 3 entre 1 e {n}: 3: {contador_pares}')