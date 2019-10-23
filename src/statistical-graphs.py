import statistics as st
import matplotlib.pyplot as plt
from numpy import array
import math
import csv
import json
import pandas as pd
from statisticalLib import lerCSV, statistics


x = lerCSV('./analysis_summary.csv', 'quantidade_raiz', 4 )

lista = sorted(x)

# Remove outlier (Dados não usuais em conjuntos de dados)
# x.remove(valor)

statistics(lista, 'Licenças encontradas na raiz')

parx = []
pary = []

#usa x se for para ver a dispersão ou lista se quiser ver o grafico evoluindo (e ordenado)
for a,index in enumerate(lista):
        if a % 2 == 0:
                parx.append(index)
                #print(index)
        else:
                pary.append(index)
                #print(index)


# lista.remove(728)
# pary.remove(728)
parx.pop()

# print(len(x))
# print(len(parx))
# print(len(pary))

# Numero de classes
k = round(1+3.3*math.log10(len(lista)))
print('k = {:.2f}'.format(k))

# Tamanho do intervalo de cada classe
h = (max(lista)-min(lista))/k
print('h = {:.2f}'.format(h))

# Grafico de dispersão
plt.plot(parx,pary,'o')
plt.title('Dispersão')
plt.show()

# HISTOGRAMA
plt.hist(lista, bins=k)
plt.ylabel('Quantidade de licenças no projeto') #definindo nome do eixo X
plt.xlabel('Classes de distribuição') #definindo nome do eixo Y
plt.show()

# BOX PLOT EXEMPLO
quartil = len(lista)//4

value1 = x[0:quartil]
value2 = x[quartil:quartil*2]
value3 = x[quartil*2:quartil*3]
value4 = x[quartil*3:quartil*4]

data_to_plot = [value1, value2, value3, value4]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))
# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
bp = ax.boxplot(data_to_plot)
plt.show()
# Save the figure
# fig.savefig('fig1.png', bbox_inches='tight')