# https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/licenses -> onde os textos das licenças são encontrados
import os
import csv
import json
import pandas as pd

# Busca numa string a incidêcia de uma palavra 
def wordSearch(string, stringParameter):
    return string.lower().count(stringParameter) != 0

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
        licenseAll = []
        #  Cria uma lista para armazenar as licenças encontradas na raiz do projeto
        licenseOnRoot = []
        #  Cria uma lista para armazenar as licenças encontradas fora da raiz do projeto
        licenseSPDX = []
        #  Cria uma variavel para armazenar o score da licenças encontradas
        licenseScore = 100.00
        licenseScoreRoot = 100.00
        #  Cria Variavel para verificar se o projeto tem licenças incompativeis
        compatibleLicenses = True
        compatibleLicensesRoot = True
        #  Cria variavel para salvar licenças encontradas em arquivos readme
        licenseReadme = []
        #  Cria variavel para salvar licenças encontradas em arquivos package.json
        licensePackage = []
        #  Cria variavel para salvar licenças encontradas em arquivos license
        licenseOnLicense = []
        # Variavel para para salvar se os projetos tem diferenças nas licenças listadas no readme, package.json e license
        # description = True
        if (readCSV != []) and (len(readCSV[0]) > 3):
            # Vare a lista e buscar as licenças listadas na coluna 'license_expression'e que estejam na raiz do projeto
            for row in readCSV:

                # Busca licença em todo o projeto
                if(row[4] != "") and (row[4] != "license__key"):
                    # Busca licença na raiz do projeto
                    # if(row[3] != "") and (row[3] != "license_expression") and (row[0].count('/') == 2):

                    # Se for encontrada um licença, ela é adicionada a lista
                    licenseAll.append(row[4])

                    if (row[0].count('/') == 2):
                        licenseOnRoot.append(row[4])
                        if (float(row[5]) < licenseScore):
                            licenseScoreRoot = float(row[5])
                    
                    if (float(row[5]) < licenseScore):
                        licenseScore = float(row[5])

                    # Testa se a licença é permissiva no projeto inteiro
                    if (row[8] != "Permissive"):
                        compatibleLicenses = False

                    # Testa se a licença é permissiva em licenças encontradas na raiz do projeto 
                    if (row[8] != "Permissive") and (row[0].count('/') == 2):
                        compatibleLicensesRoot = False

                    # Salva as licenças encontradas em arquivos readme
                    if (wordSearch(row[0],'readme')) and (row[0].count('/') == 2):
                        licenseReadme.append(row[4])

                    # Salva as licenças encontradas em arquivos package.json
                    if (wordSearch(row[0],'package.json')) and (row[0].count('/') == 2):
                        licensePackage.append(row[4])

                    # Salva as licenças encontradas em arquivos de license
                    if (wordSearch(row[0],'license')) and (row[0].count('/') == 2):
                        licenseOnLicense.append(row[4])
                    
                if(row[14] != "") and (row[14] != "license__spdx_license_key"):
                    # Se for encontrada um licença SPDX, ela é adicionada a lista
                    licenseSPDX.append(row[14])

    # if (licenseReadme == []):
    #     description = (licensePackage.sort() == licenseOnLicense.sort())
    # elif (licenseOnLicense == []):
    #     description = (licensePackage.sort() == licenseReadme.sort())
    # elif (licensePackage == []):
    #     description = True
    # else:
    #     description = (licensePackage.sort() == licenseReadme.sort() == licenseOnLicense.sort())

    # if (licensePackage != []):
    #     description =  ( licensePackage.sort() == (licenseOnLicense + licenseReadme).sort() ) 

    
    # Testa se a licença ta duplicada no projeto
    # Testa se a lista não é vazia
    if licenseAll == []:
        # Se for vazia adiciona verdadeiro para a varial de teste
        duplicadoGeral = True
    else:
        # Cria variavel que denota se existe mais de uma licença na lista
        duplicadoGeral = False
        #  Cria uma variavel que armazena o primeiro valor da lista de licenças
        swap = licenseAll[0]
        # Loop para checar se existe mais de uma licença na lista
        for pizza in licenseAll:
            if (pizza != swap):
                duplicadoGeral = True
                break
    
    # Testa se a licença ta duplicada na raiz do projeto
    # Testa se a lista não é vazia
    if licenseOnRoot == []:
        # Se for vazia adiciona verdadeiro para a varial de teste
        duplicadoRoot = True
    else:
        # Cria variavel que denota se existe mais de uma licença na lista
        duplicadoRoot = False
        #  Cria uma variavel que armazena o primeiro valor da lista de licenças
        swap = licenseOnRoot[0]
        # Loop para checar se existe mais de uma licença na lista
        for pizza in licenseOnRoot:
            if (pizza != swap):
                duplicadoRoot = True
                break

    # Retorna o resultado da função
    return {
        "nome": readCSV[1][0],
        "duplicado_geral":duplicadoGeral,
        "duplicado_raiz":duplicadoRoot,
        "quantidade_geral":len(set(licenseAll)),
        "quantidade_raiz":len(set(licenseOnRoot)),
        "licenca_SPDX":len(set(licenseSPDX)),
        "license_score_geral":licenseScore,
        "license_score_raiz":licenseScoreRoot,
        "licencas_compativeis_geral":compatibleLicenses,
        "licencas_compativeis_raiz":compatibleLicensesRoot,
        "licencas_readme":len(set(licenseReadme)),
        "licencas_packageJson":len(set(licensePackage)),
        "licencas_license":len(set(licenseOnLicense)),
        # "compatibilidade_descrições":description
        }

# Com licença duplicada [node]
# print(licencaDuplicada('./summary-licenses-csv/license14.csv'))


with open('analysis_summary.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = [
        'nome',
        'duplicado_geral',
        'duplicado_raiz',
        'quantidade_geral',
        'quantidade_raiz',
        'licenca_SPDX',
        'license_score_geral',
        'license_score_raiz',
        'licencas_compativeis_geral',
        'licencas_compativeis_raiz',
        'licencas_readme',
        'licencas_packageJson',
        'licencas_license',
        # 'compatibilidade_descrições'
        ]
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