from _operator import length_hint
import matplotlib.pyplot as plt
import numpy as np
import math
import csv
import collections
notas = [1,2,3,4,5,6,7,8,9,10]
li = []
lo = []
rep = []
prob = []
probacu = []

with open('notas.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        list.append(li,int(row[0]))



with open('resul.csv', 'w', newline = '') as file:
        spamwriter = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerows([rep])





def con (lo,rep):
    t = 10
    i = 1
    while i <= t:
        rep.append(lo[i])
        i +=1
    return rep


def prob_uni (rep,prob):
    t = 9
    i = 0
    res = 0
    while i <= t:
        res = rep[i] / length_hint(li)
        res = round(res,2)
        prob.append(res)
        i += 1
    return rep

    return prob

def prob_acum (prob,probacu):
    t = 9
    i = 0
    res = 0
    while i <= t:
        res = res + prob[i]
        res =round(res,2)
        probacu.append(res)
        i += 1

    return probacu


if __name__ == '__main__':
    print('Puntaje---------->','-',notas[0],'-','-',notas[1],'-','-',notas[2],'-','-',notas[3],'-','-',notas[4],'-','-',notas[5],'-','-',notas[6],'-','-',notas[7],'-','-',notas[8],'-','-',notas[9])
    lo = collections.Counter(li)
    con(lo, rep)
    prob_uni(rep,prob)
    prob_acum(prob,probacu)
    print('repeticiones----->','-',rep[0],'-','-',rep[1],'-','-',rep[2],'-','-',rep[3],'-','-',rep[4],'-','-',rep[5],'-','-',rep[6],'-','-',rep[7],'-','-',rep[8],'-','-',rep[9])
    print('probabilidad----->',prob)
    print('prob. acumulada->',probacu)

    plt.style.use('_mpl-gallery')


    # plot
    fig, ax = plt.subplots()

    ax.bar(notas, prob, width=0.7, edgecolor="white", linewidth=1)

    ax.set(xlim=(0, 10), xticks=np.arange(1,10),
           ylim=(0, 1), yticks=np.arange(1))

    plt.show()
