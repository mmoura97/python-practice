import openpyxl
novo_workbook = openpyxl.Workbook() #Criando uma nova pasta de trabalho
print("Nova pasta de trabalho criada.")
planilha_padrao = novo_workbook.active
print(f"Planilha padrão: {planilha_padrao.title} ") #Por padrão ela vem chamada de Sheet
planilha_padrao.title = "Dados Principais" #Renomeando a planilha padrão
print(f"Planilha padrão renomeada para: {planilha_padrao.title}")
print ("Nomes das planilhas no novo workbook:",novo_workbook.sheetnames) #Verificando as planilhas criadas
planilha_dados = novo_workbook["Dados Principais"] #Adicionando dados

planilha_dados["A1"] = "1"
planilha_dados["B1"] = "10.01"
planilha_dados["A2"] = "2"
planilha_dados["B2"] = 9.98
planilha_dados["A3"] = "3"
planilha_dados["B3"] = 10.02
planilha_dados["A4"] = "4"
planilha_dados["B4"] = "9.99"
planilha_dados["A5"] = "5"
planilha_dados["B5"] = 10.00
planilha_dados["A6"] = "6"
planilha_dados["B6"] = 10.03
planilha_dados["A7"] = "7"
planilha_dados["B7"] = 9.97
planilha_dados["A8"] = "8"
planilha_dados["B8"] = 10.01
planilha_dados["A9"] = "9"
planilha_dados["B9"] = 10.02 
planilha_dados["A10"] = "10"
planilha_dados["B10"] = 10.03
nome_novo_arquivo = "Controle_Qualidade.xlsx"
try:
    novo_workbook.save (nome_novo_arquivo) #Salvando arquivo
    print(f"Nova pasta de trabalho salva como(nome novo arquivo) ")
except Exception as e:
    print(f"Erro ao salvar o novo arquivo: (e)")
