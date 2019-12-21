# https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/licenses -> onde os textos das licenças são encontrados
import subprocess
import os
import csv

# Busca numa string a incidêcia de uma palavra 
def wordSearch(string, stringParameter):
    return string.lower().count(stringParameter) != 0

# Função que retorna se um repositorio tem mais de uma licença
def licencaDuplicada(file, numero):
    # Abre o arquivo .csv definidor
    with open(file) as csvfile:
        # Adiciona os valores a um objeto, onde cada item vai ser uma linha
        temp = csv.reader(csvfile, delimiter=',')
        # Cria lista que vai receber os dados do objeto
        readCSV = []
        # Transforma o objeto em uma lista
        for line in temp:
            readCSV.append(line)
        #entra no repositorio
        pathGlobal = readCSV[1][0].replace('/[','').replace(']',' ').replace('/',' ',1).split(' ')
        os.chdir("repositories/["+pathGlobal[0]+"]"+pathGlobal[1]+"/")
        print("Projeto "+str(numero)+": "+pathGlobal[1])
        if (readCSV != []) and (len(readCSV[0]) > 3):
            # Vare a lista e buscar as licenças listadas na coluna 'license_expression'e que estejam na raiz do projeto
            for row in readCSV:
                path = []
                #Encontra a ocorrencia de arquivos com licenças
                if(row[4] != "") and (row[4] != "license__key") and (row[0].count('/') == 2) and (wordSearch(row[0],'licen')):
                    path = row[0].replace('/[','').replace(']',' ').replace('/',' ',1).split(' ')
                    # subprocess.getoutput("git shortlog -sen "+path[2]+" >> ~/Desktop/testegitlog.txt")
                    subprocess.getoutput("git log --pretty=format:'%H;%an;%ae' "+path[2]+" >> ~/Desktop/arqTemp.txt")     
        subprocess.getoutput("awk -F ';' '!x[$2]++''{print}' ~/Desktop/arqTemp.txt >> ~/Desktop/arqTemp1.txt")                     
        os.system("sed 's/^/"+pathGlobal[1]+";https:\/\/github.com\/"+pathGlobal[0]+"\/"+pathGlobal[1]+";/' ~/Desktop/arqTemp1.txt >> ~/Desktop/TodosOscomiter.csv") 
        os.system("echo > ~/Desktop/arqTemp.txt")
        os.system("echo > ~/Desktop/arqTemp1.txt")
        os.chdir("../..")              
        # os.system("sed 's/^/"+pathGlobal[1]+";/' ~/Desktop/arqTemp.txt >> ~/Desktop/TodosOscomiter.txt")               
        # print("sed 's/^/"+pathGlobal[1]+";github.com/"+pathGlobal[0]+"/"+pathGlobal[1]+";/' ~/Desktop/arqTemp.txt > ~/Desktop/TodosOscomiter.txt")               



inicio = 0
fim = 1553

for sorvete in range(inicio, fim):
    if (os.path.isfile(f'./summary-licenses-csv/license{str(sorvete)}.csv') == True) :
        licencaDuplicada(f'./summary-licenses-csv/license{str(sorvete)}.csv', sorvete)