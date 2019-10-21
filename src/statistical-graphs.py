import statistics as st
import matplotlib.pyplot as plt
from numpy import array
import math
import csv
import json
import pandas as pd



with open('./analysis_summary.csv') as csvfile:
    # Adiciona os valores a um objeto, onde cada item vai ser uma linha
    temp = csv.reader(csvfile, delimiter=',')
    # Cria lista que vai receber os dados do objeto
    readCSV = []
    # Transforma o objeto em uma lista
    for line in temp:
        readCSV.append(line)

    x = []

    for row in readCSV:
        # Busca licença em todo o projeto
        if(row[3] != "quantidade_geral"):
            x.append(int(row[3]))



# x = [11 , 5 , 2 , 0 , 9 , 9 , 1 , 5 , 1 , 3 ,3 , 3 , 7 , 4 , 12 , 8 , 5 , 2 , 6 , 1 ,11 , 1 , 2 , 4 , 2 , 1 , 3 , 9 , 0 , 10 ,3 , 3 , 1 , 5 , 18 , 4 , 22 , 8 , 3 , 0 ,8 , 9 , 2 , 3 , 12 , 1 , 3 , 1 , 7 , 5 ,14 , 7 , 7 , 28 , 1 , 3 , 2 , 11 , 13 , 2 ,0 , 1 , 6 , 12 , 15 , 0 , 6 , 7 , 19 , 1 ,1 , 9 , 1 , 5 , 3 , 17 , 10 , 15 , 43 , 2 ,6 , 1 , 13 , 13 , 19 , 10 , 9 , 20 , 19 , 2 ,27 , 5 , 20 , 5 , 10 , 8 , 2 , 3 , 1 , 1 ,4 , 3 , 6 , 13 , 10 , 9 , 1 , 1 , 3 , 9 ,9 , 4 , 0 , 3 , 6 , 3 , 27 , 3 , 18 , 4 ,6 , 0 , 2 , 2 , 8 , 4 , 5 , 1 , 4 , 18 ,1 , 0 , 16 , 20 , 2 , 2 , 2 , 12 , 28 , 0 ,7 , 3 , 18 , 12 , 3 , 2 , 8 , 3 , 19 , 12 ,5 , 4 , 6 , 0 , 5 , 0 , 3 , 7 , 0 , 8 ,8 , 12 , 3 , 7 , 1 , 3 , 1 , 3 , 2 , 5 ,4 , 9 , 4 , 12 , 4 , 11 , 9 , 2 , 0 , 5 ,8 , 24 , 1 , 5 , 12 , 9 , 17 , 728 , 12 , 6 ,4 , 3 , 5 , 7 , 4 , 4 , 4 , 11 , 3 , 8 ]
# Ordena a lista 
lista = sorted(x)

# Remove outlier (Dados não usuais em conjuntos de dados)
lista.remove(252)
lista.remove(236)
lista.remove(240)
lista.remove(208)
lista.remove(235)
lista.remove(256)

print(lista)
print(len(lista)/4)

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

print('- MEDIDAS DE CENTRALIDADE')
print('Media = {:.2f}'.format(media))                                
print('Mediana = {:.2f}'.format(mediana))
print('Moda = '+ str(moda) )
print('Minimo = ' + str(minimo) )
print('Maximo = ' + str(maximo) )
print('- MEDIDAS DE DISPERSÃO')
print('Ampĺitude = ' + str(amplitude) )
print('Desvio Padrão = {:.2f}'.format(desvio))
print('Variança = {:.2f}'.format(varianca))
print('Coeficiente de Variação = {:.2f} %'.format(coeficiente_var))
print('Coeficiente de Assimetria = {:.3f}'.format(coeficiente_ass))
print('Q1 = '+ str(Q1))
print('Q2 = '+ str(Q2))
print('Q3 = '+ str(Q3))


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


#Numero de classes
k = round(1+3.3*math.log10(len(lista)))
print('k = {:.2f}'.format(k))

#Tamanho do intervalo de cada classe
h = (max(lista)-min(lista))/k
print('h = {:.2f}'.format(h))

# Grafico de dispersão
# plt.plot(parx,pary,'o')
# plt.show()

#HISTOGRAMA
# plt.hist(lista, bins=k)
# plt.show()

# BOX PLOT EXEMPLO
# value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
# value2 = [62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
# value3 = [23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
# value4 = [59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]
quartil = len(lista)//4

value1 = lista[0:quartil]
value2 = lista[quartil:quartil*2]
value3 = lista[quartil*2:quartil*3]
value4 = lista[quartil*3:quartil*4]

box_plot_data=[value1,value2,value3,value4]
box=plt.boxplot(box_plot_data,vert=0,patch_artist=True,labels=['Q1','Q2','Q3','Q4'],
            )
 
colors = ['cyan', 'lightblue', 'lightgreen', 'tan']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
 
plt.show()