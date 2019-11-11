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
        sum(lerCSV(arquivoCSV, 'licencas_license', 12)),
        sum(lerCSV(arquivoCSV, 'licencas_outros_arquivos', 13))
        ]
# ESTATISTICAS GERAIS
# Licenças conhecidas pela SPDX
pizza(
        [sum(spdx), (sum(qtd_geral) - sum(spdx))],
        ['Reconhecidas', 'Não reconhecidas'],
        'Licenças conhecidas pela SPDX',
        'pizza_licencas_conhecidas'
)
statistics(qtd_geral, "Licenças por projeto com outlier")
# Histograma distribuição de frequencia
# das licencas encontradas no projeto geral
for outlier in detect_outlier(qtd_geral): # remove outliers
        qtd_geral.remove(outlier)
statistics(qtd_geral, "Licenças por projeto sem outlier")
histograma(
        qtd_geral,
        'Distribuição de frequencia de qtd de licenças por projeto - geral',
        'Classes de distribuição',
        'Quantidade de licenças no projeto',
        'hit_qtd_projeto'
)

# Histograma distribuição de frequencia
# das licencas encontradas na rais do projeto
for outlier in detect_outlier(qtd_raiz): # remove outliers
        qtd_raiz.remove(outlier)

histogramaSelectK(
        qtd_raiz,
        'Distribuição de frequencia de qtd de licenças por projeto - raiz',
        'Classes de distribuição',
        'Quantidade de licenças no projeto',
        'hit_qtd_raiz',
        7
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
        ['Readme', 'Package.json', 'License', 'Outros Arquivos'],
        'Localização das licenças por tipo de arquivo',
        'barras_local_licencas'
)