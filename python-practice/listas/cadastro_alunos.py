# Exercicios - cadastro_alunos

def quantidade_de_alunos():
  while True:
    try:
      alunos = int(input('Digite a quantidade de alunos (minimo 3 alunos): \n'))
      if alunos >= 3:
        return alunos
      else:
        print('Erro, quantidade minima não atingida!')
    except ValueError:
      print('Erro, caracter invalido, Digite um numero valido!')


def obter_nota():
  while True:
    try:
      nota = float(input('Digite a nota do aluno: \n '))
      if nota >= 0 and nota <=10:
        return nota
      else:
        print('Erro, a nota deve ser entre 0 e 10')
    except ValueError:
      print('Erro, caracter invalido, Digite um numero valido!')


nomes = []
notas = []

num_de_alunos = quantidade_de_alunos()
for i in range(num_de_alunos):
  nome_aluno = input('Digite o nome de Aluno: \n')
  nota_aluno = obter_nota()
  nomes.append(nome_aluno)
  notas.append(nota_aluno)

print("\n--- Cadastro Concluído! ---")

media_geral = sum(notas) / len(notas)

maior_nota = max(notas)
indice_maior = notas.index(maior_nota)
nome_maior = nomes[indice_maior]

min_nota = min(notas)
indice_min = notas.index(min_nota)
nome_min = nomes[indice_min]

alunos_acima_da_media = 0
for nota in notas:
  if nota > media_geral:
    alunos_acima_da_media += 1


print("\n--- Essa é a lista Cadastrada ---")
print(nomes)
print(notas)
print("\n--- Media Geral da Turma ---")
print(f"Essa é a media geral da Turma {media_geral}")
print(f"Aluno {nome_maior} esta com a maior nota: {maior_nota})")
print(f"Aluno {nome_min} esta com a menor nota: {min_nota})")
print(f"Aluno acima da media {alunos_acima_da_media})")