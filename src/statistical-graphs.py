import statistics as st
import matplotlib.pyplot as plt
from numpy import array
import math
import pandas as pd
from statisticalLib import *

# Define as listas de valores
arquivoCSV = './analysis_summary.csv'
dup_geral = lerCSV(arquivoCSV, 'duplicado_geral', 1 )
dup_raiz = lerCSV(arquivoCSV, 'duplicado_raiz', 2 )
qtd_geral = lerCSV(arquivoCSV, 'quantidade_geral', 3 )
qtd_raiz = lerCSV(arquivoCSV, 'quantidade_raiz', 4 )
spdx = lerCSV(arquivoCSV, 'licenca_SPDX', 5 )
comp_geral = lerCSV(arquivoCSV, 'licencas_compativeis_geral', 8 )
comp_raiz = lerCSV(arquivoCSV, 'licencas_compativeis_raiz', 9 )
locate_licenses = [
        sum(lerCSV(arquivoCSV, 'licencas_readme', 10)),
        sum(lerCSV(arquivoCSV, 'licencas_packageJson', 11)),
        sum(lerCSV(arquivoCSV, 'licencas_license', 12))
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

# Arquivos onde as licenças são encontradas
barras(
        locate_licenses,
        ['Readme', 'Package.json', 'License'],
        'Localização das licenças por tipo de arquivo',
        'barras_local_licencas'
)