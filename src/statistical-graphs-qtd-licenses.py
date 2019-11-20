import statistics as st
import matplotlib.pyplot as plt
from numpy import array
import math
import pandas as pd
from statisticalLib import *

with open('./listaDeLicenças.txt') as csvfile:
        # Adiciona os valores a um objeto, onde cada item vai ser uma linha
        temp = csv.reader(csvfile, delimiter=',')
        # Cria lista que vai receber os dados do objeto
        readCSV = []
        # Transforma o objeto em uma lista
        for line in temp:
                readCSV.append(line)
        licenses = []
        for row in readCSV:
                licenses.append(row[0])

        resumo = set(licenses)
        quantidade = []
        for qtd in resumo:
                quantidade.append(licenses.count(qtd))

        licencasResumo = ['mit','apache-2.0','bsd-new','facebook-patent-rights-2','generic-cla','Outras Licenças']
        quantidadeResumo = [78704,52174,44671,10329,9312, 64167]
        print(sum(quantidadeResumo))
        print(quantidade)
        print(licenses)
   
        fig1, ax1 = plt.subplots()
        ax1.pie(quantidadeResumo, labels = licencasResumo, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')
        plt.title('Licenças Com Maior Insidencia')
        plt.savefig('./graphs/licencas_comuns.png', bbox_inches='tight')
        plt.show()