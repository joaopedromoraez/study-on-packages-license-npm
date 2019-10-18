# scancode-toolkit/src/licensedcode/data/licenses/ -> onde os textos das licenças são encontrados
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
        #  Cria uma lista para armazenar as licenças encontradas na raiz do projeto
        licenseOnRoot = []
        #  Cria uma lista para armazenar as licenças encontradas fora da raiz do projeto
        licenseSPDX = []
        #  Cria uma variavel para armazenar o score da licenças encontradas
        licenseScore = 100.00
        licenseScoreRoot = 100.00

        if (readCSV != []) and (len(readCSV[0]) > 3):
            # Vare a lista e buscar as licenças listadas na coluna 'license_expression'e que estejam na raiz do projeto
            for row in readCSV:

                # Busca licença em todo o projeto
                if(row[4] != "") and (row[4] != "license__key"):
                    # Busca licença na raiz do projeto
                    # if(row[3] != "") and (row[3] != "license_expression") and (row[0].count('/') == 2):

                    # Se for encontrada um licença, ela é adicionada a lista
                    license.append(row[4])

                    if (row[0].count('/') == 2):
                        licenseOnRoot.append(row[4])
                        if (float(row[5]) < licenseScore):
                            licenseScoreRoot = float(row[5])
                    
                    if (float(row[5]) < licenseScore):
                        licenseScore = float(row[5])
                    
                if(row[14] != "") and (row[14] != "license__spdx_license_key"):
                    # Se for encontrada um licença SPDX, ela é adicionada a lista
                    licenseSPDX.append(row[14])


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
    return {"nome": readCSV[1][0],"duplicado":testar, "quantidade_total":len(set(license)), "licenca_na_raiz":len(set(licenseOnRoot)), "licenca_SPDX":len(set(licenseSPDX)), "license_score":licenseScore, "license_score_in_root":licenseScoreRoot}

# Com licença duplicada [node]
# print(licencaDuplicada('./summary-licenses-csv/license14.csv'))


with open('dados_teste.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['nome','duplicado', 'quantidade_total', 'licenca_na_raiz', 'licenca_SPDX','license_score','license_score_in_root']
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