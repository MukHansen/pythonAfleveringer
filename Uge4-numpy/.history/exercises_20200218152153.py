import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

filename = './befkbhalderstatkode.csv'

data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def getSomething(hood):
    deezMask = (data[:,1] == hood) & (data[:,0] == 2015)
    return np.sum(data[deezMask][:,4])

def getSumPerHood():
    lst = {}
    for key, value in neighb.items():
        # print(value, getSomething(key))
        lst.update({value: getSomething(key)})
    return lst

# print(getSumPerHood())

def whatever():
    lst = getSumPerHood()
    hoodsSorted = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
    hoodsSorted = sorted(lst.items(), key=operator.itemgetter(1))
    cityAreas = []
    sumOfPeople = []
    for key, value in hoodsSorted.items():
        cityAreas.append(key)
        sumOfPeople.append(value)

    plt.bar(cityAreas, sumOfPeople, width=0.5, linewidth=0, align='center')
    title = 'Population in various areas '
    plt.title(title, fontsize=12)
    plt.ticklabel_format(useOffset=False)
    plt.xticks(data[:,2]) # DETTE VIL KUN SKRIVE TALLET
    plt.ticklabel_format(useOffset=False)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()

whatever()