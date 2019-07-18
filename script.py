import os
import csv

#Name[0];Stars[1];Forks[2];Language[3];Description[4];URL[5];Domain[6];Growth Pattern[7]

with open('Domains of 5,000 GitHub Repositories - Public - Domains.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #salva todos os links do csv
    repositorios = [] 
    for row in readCSV:
        if(row[3] == "JavaScript"):
            #row[5] é a coluna que contem os links
            projeto = []
            projeto.append(row[0].split("/")[1])
            projeto.append(row[5])
            repositorios.append(projeto)

os.system("mkdir repositorios")

for pizza in range(51, 52):
    print(repositorios[pizza])
    os.system("git clone " + repositorios[pizza][1] + " repositorios/" + repositorios[pizza][0])

# print(len(repositorios)) 

