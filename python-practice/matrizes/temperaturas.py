# Exercicios - temperaturas

def obter_temperaturas():
  while True:
    try:
      temperatura = float(input('Digite a temperatura em graus Celsius: \n'))
      return temperatura
    except ValueError:
      print('Erro, caracter invalido, Digite um numero valido!')

matriz_temperaturas = []
numero_semanas = 3
numero_dias = 4
soma_geral = 0
contador_total_dias = 0
contador_semana = 1

for i in range(numero_semanas):
  semanas_atual = []
  for j in range(numero_dias):
    print(f"Digite a temperatura do dia {j+1} da semana {i+1}:")
    temp_lida = obter_temperaturas()
    semanas_atual.append(temp_lida)
  matriz_temperaturas.append(semanas_atual)

print("\n--- Temperatura Cadastrada ---")
print()
print("A matriz resultante é: ")
for semana in matriz_temperaturas:
    print(semana)


for semana in matriz_temperaturas:
    soma_da_semana = sum(semana)
    media_da_semana = soma_da_semana / len(semana)
    soma_geral += soma_da_semana
    contador_semana = matriz_temperaturas.index(semana) + 1
    print(f"Média da Semana {contador_semana}: {media_da_semana:.2f}")

contagem_total_de_dias = numero_semanas * numero_dias
media_geral = soma_geral / contagem_total_de_dias
print(f"Média Geral de todas as semanas: {media_geral:.2f}")

maior_temp_geral = matriz_temperaturas[0][0]
menor_temp_geral = matriz_temperaturas[0][0]

for semana in matriz_temperaturas:
    for temperatura in semana:
        if temperatura > maior_temp_geral:
            maior_temp_geral = temperatura
        if temperatura < menor_temp_geral:
            menor_temp_geral = temperatura

print(f"A MAIOR temperatura registrada foi: {maior_temp_geral}")
print(f"A MENOR temperatura registrada foi: {menor_temp_geral}")