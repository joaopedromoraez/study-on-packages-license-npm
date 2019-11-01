import statistics as st
import matplotlib.pyplot as plt
from numpy import array
import math
import pandas as pd
from statisticalLib import *

#Define funções para gerar os graficos
def pizza(valores, labels, titulo, arquivo):        
        fig1, ax1 = plt.subplots()
        ax1.pie(valores, labels = labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')
        plt.title(titulo)
        plt.savefig(f'./graphs/{arquivo}.png', bbox_inches='tight')
        plt.show()

def histograma(valores, titulo, labelX, labelY, arquivo):
        k = round(1+3.3*math.log10(len(valores)))
        plt.hist(valores, rwidth=0.9, bins=k)
        plt.title(titulo)
        plt.xlabel(labelX)
        plt.ylabel(labelY)
        plt.grid(axis='y', alpha=0.9)
        plt.savefig(f'./graphs/{arquivo}.png', bbox_inches='tight')
        plt.show()

# Define as listas de valores
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

histograma(
        lista01,
        'Distribuição de frequencia de qtd de licenças por projeto - geral',
        'Classes de distribuição',
        'Quantidade de licenças no projeto',
        'hit_qtd_projeto'
)

# HISTOGRAMA
lista02 = list(filter(lambda a: a != 1 and a != 0, qtd_raiz))
histograma(
        lista02,
        'Distribuição de frequencia de qtd de licenças por projeto - raiz',
        'Classes de distribuição',
        'Quantidade de licenças no projeto',
        'hit_qtd_raiz'
)

# Grafico de pizza Projeto com mais de um licença - Geral
pizza(
        [dup_geral.count('True'), dup_geral.count('False')],
        ['Mais de uma licença', 'Uma licença'],
        'Proporção de projetos com mais de uma licença - Geral',
        'pizza_lic_geral'
)

# Grafico de pizza Projeto com mais de um licença - Raiz
pizza(
        [dup_raiz.count('True'), dup_raiz.count('False')],
        ['Mais de uma licença', 'Uma licença'],
        'Proporção de projetos com mais de uma licença - Raiz',
        'pizza_lic_raiz'
)

# Compatibilidade de Licenças - Geral
pizza(
        [comp_geral.count('True'), comp_geral.count('False')],
        ['Compativeis', 'Não Compativeis'],
        'Compatibilidade de Licenças - Geral',
        'pizza_compatibilidade_geral'
)

# Compatibilidade de Licenças - Raiz
pizza(
        [comp_raiz.count('True'), comp_raiz.count('False')],
        ['Compativeis', 'Não Compativeis'],
        'Compatibilidade de Licenças - Raiz',
        'pizza_compatibilidade_raiz'
)

# Onde as licenças são encontradas
labels1 = ['Readme', 'Package.json', 'License']
plt.bar(labels1, locate_licenses, color='green')
plt.title("Localização das licenças por tipo de arquivo")
plt.savefig('./graphs/barras_local_licencas.png', bbox_inches='tight')
plt.show()