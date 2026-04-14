# Exercício 1 - Conversor de Moedas

print("Conversor de Moedas!!")

reais = float(input("Digite o valor em Reais que deseja converter: "))

dolar = reais/5.50
euro = reais/6.33
pesoArgentino =  reais/0.0038
libraEsterlina = reais/7.31


print(f"O valor convertido para Dólar é de ${dolar:.2f}")
print(f"O valor convertido para Euro é de €{euro:.2f}")
print(f"O valor convertido para Peso Argentino é de ${pesoArgentino:.2f}")
print(f"O valor convertido para Libra Esterlina é de £{libraEsterlina:.2f}")