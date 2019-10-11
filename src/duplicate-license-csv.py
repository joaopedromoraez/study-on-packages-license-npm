import os
import csv
import json
import pandas as pd

# Função que retorna se um repositorio tem mais de uma licença
def licencaDuplicada(file):
    # Abre o arquivo .csv definidor
    with open(file) as csvfile:
        # Adiciona os valores a um objeto, onde cada item vai ser uma linha
        temp = csv.reader(csvfile, delimiter=',')
        # Cria lista que vai receber os dados do objeto
        readCSV = []
        # Transforma o objeto em uma lista
        for line in temp:
            readCSV.append(line)
        #  Cria uma lista para armazenar as licenças encontradas
        license = []
        if (readCSV != []) and (len(readCSV[0]) > 3):
            # Vare a lista e buscar as licenças listadas na coluna 'license_expression'e que estejam na raiz do projeto
            for row in readCSV:

                # Busca licença em todo o projeto
                if(row[3] != "") and (row[3] != "license_expression"):
                    # Busca licença na raiz do projeto
                    # if(row[3] != "") and (row[3] != "license_expression") and (row[0].count('/') == 2):

                    # Se for encontrada um licença, ela é adicionada a lista
                    license.append(row[3])
    # Testa se a lista não é vazia
    if license == []:
        # Se for vazia adiciona verdadeiro para a varial de teste
        testar = True
    else:
        # Cria variavel que denota se existe mais de uma licença na lista
        testar = False
        #  Cria uma variavel que armazena o primeiro valor da lista de licenças
        swap = license[0]
        # Loop para checar se existe mais de uma licença na lista
        for pizza in license:
            if (pizza != swap):
                testar = True
                break
    
    # Retorna o resultado da função
    return {"nome": readCSV[1][0],"duplicado":testar, "quantidade":len(set(license))}

# Com licença duplicada [node]
# print(licencaDuplicada('./summary-licenses-csv/license14.csv'))


with open('dados_teste.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['nome','duplicado', 'quantidade']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    # writer.writerow(licencaDuplicada('./summary-licenses-csv/license14.csv'))

    inicio = 0
    fim = 1553

    for sorvete in range(inicio, fim):
        if (os.path.isfile(f'./summary-licenses-csv/license{str(sorvete)}.csv') == True) :
            writer.writerow(licencaDuplicada(f'./summary-licenses-csv/license{str(sorvete)}.csv'))
            name = licencaDuplicada(f'./summary-licenses-csv/license{str(sorvete)}.csv')['nome'].replace("/","")
            print(f'{str(sorvete)} - {name}')