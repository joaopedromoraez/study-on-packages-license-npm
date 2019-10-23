import statistics as st
import matplotlib.pyplot as plt
from numpy import array
import math
import csv
import json
import pandas as pd

def lerCSV(arquivo, titulo_coluna, indice_coluna):
    with open(arquivo) as csvfile:
        # Adiciona os valores a um objeto, onde cada item vai ser uma linha
        temp = csv.reader(csvfile, delimiter=',')
        # Cria lista que vai receber os dados do objeto
        readCSV = []
        # Transforma o objeto em uma lista
        for line in temp:
            readCSV.append(line)

        lista = []

        for row in readCSV:
            if(row[indice_coluna] != titulo_coluna):
                lista.append(int(row[indice_coluna]))
        return lista


def statistics(x, name_lista):
    lista = sorted(x)
    # Média é a soma dos valores de elementos dividido pela quantidade de elementos.
    media = st.mean(lista)
    # Mediana é o valor que divide o conjunto X pela metade
    mediana = st.median(lista)
    # Moda é o valor que aparece com mais frequência no conjunto.
    moda = st.mode(lista)
    # Mínimo é o menor valor pertencente ao conjunto.
    minimo = min(lista)
    # Máximo é o maior valor pertencente ao conjunto.
    maximo = max(lista)
    # Amplitude é a diferença entre o valor máximo e o valor mínimo do conjunto.
    amplitude = max(lista) - min(lista)
    # Desvio Padrão identifica o quão próximo ou longe da média estão os elementos do conjunto. O cálculo do desvio padrão é dado pela raiz quadrada da variância.
    desvio = st.stdev(lista)
    # Variância é uma medida de dispersão que indica o quão longe os valores estão da média do conjunto. A fórmula matemática é dada pela soma do quadrado da diferença de cada valor para a média, dividido pelo número de elementos, conforme abaixo:
    varianca = st.variance(lista)
    # Coeficiente de Variação é a razão entre o desvio padrão e a variância
    coeficiente_var = st.stdev(lista) / st.mean(lista) * 100
    # Coeficiente de Assimetria identifica assimetrias no gráfico da função de densidade do conjunto. Um valor positivo indica uma elevação na esquerda, enquanto um negativo indica uma elevação na direita.
    coeficiente_ass = st.median(lista[len(lista)//2:]) / (st.median(lista) ** 3/2)
    # Quartis são valores que dividem o conjunto em subconjuntos com 25% dos elementos, cada.
    Q1 = st.median(lista[:len(lista)//2])
    Q2 = st.median(lista)
    Q3 = st.median(lista[len(lista)//2:])
    print(f'=====| {name_lista} |=====')
    print('# MEDIDAS DE CENTRALIDADE')
    print('- Media = {:.2f}'.format(media))                                
    print('- Mediana = {:.2f}'.format(mediana))
    print('- Moda = '+ str(moda) )
    print('- Minimo = ' + str(minimo) )
    print('- Maximo = ' + str(maximo) )
    print('# MEDIDAS DE DISPERSÃO')
    print('- Ampĺitude = ' + str(amplitude) )
    print('- Desvio Padrão = {:.2f}'.format(desvio))
    print('- Variança = {:.2f}'.format(varianca))
    print('- Coeficiente de Variação = {:.2f} %'.format(coeficiente_var))
    print('- Coeficiente de Assimetria = {:.3f}'.format(coeficiente_ass))
    print('- Q1 = '+ str(Q1))
    print('- Q2 = '+ str(Q2))
    print('- Q3 = '+ str(Q3))


    class objeto:
        def __init__(self, media, mediana, moda, minimo, maximo, amplitude, desvio, varianca, coeficiente_var, coeficiente_ass, q1, q2, q3 ):
            self.media = media
            self.mediana = mediana
            self.moda = moda
            self.minimo = minimo
            self.maximo = maximo
            self.amplitude = amplitude
            self.desvio = desvio
            self.varianca = varianca
            self.coeficiente_var = coeficiente_var
            self.coeficiente_ass = coeficiente_ass
            self.q1 = Q1
            self.q2 = Q2
            self.q3 = Q3

    return objeto( media, mediana, moda, minimo, maximo, amplitude, desvio, varianca, coeficiente_var, coeficiente_ass, Q1, Q2, Q3 )


# x = [11 , 5 , 2 , 0 , 9 , 9 , 1 , 5 , 1 , 3 ,3 , 3 , 7 , 4 , 12 , 8 , 5 , 2 , 6 , 1 ,11 , 1 , 2 , 4 , 2 , 1 , 3 , 9 , 0 , 10 ,3 , 3 , 1 , 5 , 18 , 4 , 22 , 8 , 3 , 0 ,8 , 9 , 2 , 3 , 12 , 1 , 3 , 1 , 7 , 5 ,14 , 7 , 7 , 28 , 1 , 3 , 2 , 11 , 13 , 2 ,0 , 1 , 6 , 12 , 15 , 0 , 6 , 7 , 19 , 1 ,1 , 9 , 1 , 5 , 3 , 17 , 10 , 15 , 43 , 2 ,6 , 1 , 13 , 13 , 19 , 10 , 9 , 20 , 19 , 2 ,27 , 5 , 20 , 5 , 10 , 8 , 2 , 3 , 1 , 1 ,4 , 3 , 6 , 13 , 10 , 9 , 1 , 1 , 3 , 9 ,9 , 4 , 0 , 3 , 6 , 3 , 27 , 3 , 18 , 4 ,6 , 0 , 2 , 2 , 8 , 4 , 5 , 1 , 4 , 18 ,1 , 0 , 16 , 20 , 2 , 2 , 2 , 12 , 28 , 0 ,7 , 3 , 18 , 12 , 3 , 2 , 8 , 3 , 19 , 12 ,5 , 4 , 6 , 0 , 5 , 0 , 3 , 7 , 0 , 8 ,8 , 12 , 3 , 7 , 1 , 3 , 1 , 3 , 2 , 5 ,4 , 9 , 4 , 12 , 4 , 11 , 9 , 2 , 0 , 5 ,8 , 24 , 1 , 5 , 12 , 9 , 17 , 728 , 12 , 6 ,4 , 3 , 5 , 7 , 4 , 4 , 4 , 11 , 3 , 8 ]
# y = statistics(x,'teste')
# print(y.media)