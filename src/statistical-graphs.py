import statistics as st
import matplotlib.pyplot as plt
from numpy import array
import math
import pandas as pd
from statisticalLib import *


dup_geral = lerCSV('./analysis_summary.csv', 'duplicado_geral', 1 )
dup_raiz = lerCSV('./analysis_summary.csv', 'duplicado_raiz', 2 )
qtd_geral = lerCSV('./analysis_summary.csv', 'quantidade_geral', 3 )
qtd_raiz = lerCSV('./analysis_summary.csv', 'quantidade_raiz', 4 )
spdx = lerCSV('./analysis_summary.csv', 'licenca_SPDX', 5 )
comp_geral = lerCSV('./analysis_summary.csv', 'licencas_compativeis_geral', 8 )
comp_raiz = lerCSV('./analysis_summary.csv', 'licencas_compativeis_raiz', 9 )
locate_licenses = [
        sum(lerCSV('./analysis_summary.csv', 'licencas_readme', 10)),
        sum(lerCSV('./analysis_summary.csv', 'licencas_packageJson', 11)),
        sum(lerCSV('./analysis_summary.csv', 'licencas_license', 12))
        ]

# HISTOGRAMA
qtd_geral.remove(208)
qtd_geral.remove(235)
qtd_geral.remove(236)
qtd_geral.remove(240)
qtd_geral.remove(252)
qtd_geral.remove(256)
lista01 = list(filter(lambda a: a != 1 and a != 0, qtd_geral))
k = round(1+3.3*math.log10(len(lista01)))
plt.hist(lista01, bins=k)
plt.title('Distribuição de frequencia de qtd de licenças por projeto - geral')
plt.ylabel('Quantidade de licenças no projeto') #definindo nome do eixo X
plt.xlabel('Classes de distribuição') #definindo nome do eixo Y
plt.savefig('./graphs/hit_qtd_projeto.png', bbox_inches='tight')
plt.show()

# HISTOGRAMA
lista02 = list(filter(lambda a: a != 1 and a != 0, qtd_raiz))
k = round(1+3.3*math.log10(len(lista02)))
plt.hist(lista02, bins=k)
plt.title('Distribuição de frequencia de qtd de licenças por projeto - raiz')
plt.ylabel('Quantidade de licenças no projeto') #definindo nome do eixo X
plt.xlabel('Classes de distribuição') #definindo nome do eixo Y
plt.savefig('./graphs/hit_qtd_raiz.png', bbox_inches='tight')
plt.show()


'''
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
'''

# Grafico de pizza Projeto com mais de um licença - Geral
sizes = dup_geral.count('True'), dup_geral.count('False')
labels = 'Mais de uma licença', 'Uma licença'
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.title('Proporção de projetos com mais de uma licença - Geral')
plt.savefig('./graphs/pizza_lic_geral.png', bbox_inches='tight')
plt.show()

# Grafico de pizza Projeto com mais de um licença - Raiz
sizes = dup_raiz.count('True'), dup_raiz.count('False')
labels = 'Mais de uma licença', 'Uma licença'
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.title('Proporção de projetos com mais de uma licença - Raiz')
plt.savefig('./graphs/pizza_lic_raiz.png', bbox_inches='tight')
plt.show()

# Compatibilidade de Licenças - Geral
sizes = comp_geral.count('True'), comp_geral.count('False')
labels = 'Compativeis', 'Não Compativeis'
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.title('Compatibilidade de Licenças - Geral')
plt.savefig('./graphs/pizza_compatibilidade_geral.png', bbox_inches='tight')
plt.show()

# Compatibilidade de Licenças - Raiz
sizes = comp_raiz.count('True'), comp_raiz.count('False')
labels = 'Compativeis', 'Não Compativeis'
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.title('Compatibilidade de Licenças - Raiz')
plt.savefig('./graphs/pizza_compatibilidade_raiz.png', bbox_inches='tight')
plt.show()

# Onde as licenças são encontradas
labels1 = ['Readme', 'Package.json', 'License']
plt.bar(labels1, locate_licenses, color='green')
plt.title("Localização das licenças por tipo de arquivo")
plt.savefig('./graphs/barras_local_licencas.png', bbox_inches='tight')
plt.show()