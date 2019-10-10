import os
import csv
import json
import pandas as pd 

#Name[0];Stars[1];Forks[2];Language[3];Description[4];URL[5];Domain[6];Growth Pattern[7]
#Abre o CSV e trata os dados, retirando os repositorios de javascript e adicionando os mesmos a uma lista
with open('src/Domains_of_5,000_GitHub_Repositories_-_Public_-_Domains.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #salva todos os links do csv
    repositorios = [] 
    for row in readCSV:
        if(row[3] == "JavaScript"):
            #row[5] é a coluna que contem os links
            projeto = []
            projeto.append("["+row[0].split("/")[0]+"]"+row[0].split("/")[1])
            projeto.append(row[5])
            repositorios.append(projeto)

inicio = 1549
fim = 1550

os.chdir("./scancode-toolkit")

for pizza in range(inicio, fim):
    print(str(pizza)+' - '+repositorios[pizza][0])
    # os.system('./scancode -l --csv ../summary-licenses-csv/license'+str(pizza)+'.csv ../repositories/'+repositorios[pizza][0])
    os.system('./scancode --format json ../repositories/'+repositorios[pizza][0]+' ../summary-licenses-json/license'+str(pizza)+'.json')
    print('=============================================')
