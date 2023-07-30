
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from datagen import Data
import time
from sort import *
import sys 
import pandas as pd

sys.setrecursionlimit(10000)

DATABOUNDS = (1000,10000)
COLOR = 'white' #font color
GENERATORS = [Data.noise, Data.A, Data.up, Data.down, Data.const]
GENNAMES = ['szum', "ciąg A-kształtny", "ciąg rosnący", "ciąg malejący", 'ciąg stały']
BACKGROUND = 'black'
TESTS = 15


SORTS = ((quick_sort, 'Quick sort'), (quick_sort_r, "Quick sort random pivot"),(selection_sort, 'Selection sort'), (heap_sort, 'Heap sort'),(insertion_sort, 'Insertion sort'),(shell_sort, 'Shell sort'))
#SORTS = [(heap_sort, 'Insertion sort')]
plot_colors = {'Quick sort':'red', "Quick sort random pivot":'orange',
                'Selection sort':'blue', 'Heap sort':'green',
                  'Insertion sort':'purple', 'Shell sort':'pink'}

res = {}
for i in GENNAMES:
    res[i] = []



def benchmark(func, datagen, overdata, dmin = -1000, dmax = 1000):

    times = []
    
    for i in overdata:
        array = datagen(dmin, dmax, i)
        start = time.time()
        try:
            func(array)
        except Exception:
            raise
        stop = time.time()
        times.append(stop-start)

    return overdata, times

    

mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR


values = list(map(int, np.linspace(*DATABOUNDS, 10)))

for SORT, SORTNAME in SORTS:


    fig, ax = plt.subplots()

#set axes properties

    ax.set_xlabel('wielkość tablicy', fontsize=7)
    ax.set_ylabel('czas (s)', fontsize=7) 
    ax.set_xticks([i for i in range(1000,10001,1000)])
    ax.spines['top'].set_color(COLOR)
    ax.spines['right'].set_color(COLOR)
    ax.spines['bottom'].set_color(COLOR)
    ax.spines['left'].set_color(COLOR)
    ax.set_facecolor(BACKGROUND)

 
    maxtime = 0
    mintime = 10

    for i, datagen in enumerate(GENERATORS):
        results = []
        x, y = benchmark(SORT, datagen, values)
        x, y = np.array(x), np.array(y)

        results.append(y)
        print("Done test ", 1, ' ', SORTNAME, ' ', GENNAMES[i])

        for test in range(TESTS-1):
            _, y1 = benchmark(SORT, datagen, values)
            y1 = np.array(y1)
            results.append(y1)
            print("Done test ", test+2, ' ', SORTNAME, ' ', GENNAMES[i])
        mean = np.mean(results, axis = 0)
        std = np.std(results, axis = 0)

        
        res[GENNAMES[i]].append((SORTNAME, x, mean, std))
        
        maxtime = max(max(mean), maxtime)
        mintime = min(min(mean), mintime)
        ax.plot(x, mean, marker = '.', label = GENNAMES[i])

    
        ax.set_ylim(mintime, maxtime)
    ax.legend(loc = 'best', facecolor = BACKGROUND)








    #set figure properties
    fig.suptitle(SORTNAME, fontsize=16)
    fig.set_facecolor(BACKGROUND)
    
    fig.tight_layout()
    fig.set_size_inches(10,6)
    plt.savefig(SORTNAME+'.png')
    print("DONE " + SORTNAME)


#combined plots



fig, ax = plt.subplots(ncols = 3, nrows=2)

#set axes properties
for i in range(3):
    for j in range(2):
        if j==1 and i==2:
            break
        ax[j,i].set_xlabel('wielkość tablicy', fontsize=7)
        ax[j,i].set_ylabel('czas (s)', fontsize=7) 
        ax[j,i].spines['top'].set_color(COLOR)
        ax[j,i].spines['right'].set_color(COLOR)
        ax[j,i].spines['bottom'].set_color(COLOR)
        ax[j,i].spines['left'].set_color(COLOR)
        ax[j,i].set_facecolor(BACKGROUND)
        ax[j,i].set_yscale('log')


for i, (gen, tup) in enumerate(res.items()):
    ax[i%2, i//2].set_title(gen)

    ax[i%2, i//2].set_xticks([min(tup[1][1]), max(tup[1][1])])
    for j, data in enumerate(tup):

        name, x, y, std = data
        if i==0: ax[i%2, i//2].plot(x, y, label = name, color = plot_colors[name])
        else: ax[i%2, i//2].plot(x, y, color = plot_colors[name])

fig.legend(loc='lower right', facecolor=BACKGROUND)

ax[1,2].axis('off')

fig.suptitle('Porównanie wydajności\n(OY logarytmicznie)', fontsize=16)
fig.set_facecolor(BACKGROUND)
fig.tight_layout()
fig.set_size_inches(10,6)
plt.savefig('speed.png')


#################################################

fig, ax = plt.subplots(ncols = 3, nrows=2)

#set axes properties
for i in range(3):
    for j in range(2):
        if j==1 and i==2:
            break
        ax[j,i].set_xlabel('wielkość tablicy', fontsize=7)
        ax[j,i].set_ylabel('czas (s)', fontsize=7) 
        ax[j,i].spines['top'].set_color(COLOR)
        ax[j,i].spines['right'].set_color(COLOR)
        ax[j,i].spines['bottom'].set_color(COLOR)
        ax[j,i].spines['left'].set_color(COLOR)
        ax[j,i].set_facecolor(BACKGROUND)


temp = list(res.items())
temp = zip(*[temp[i][1]  for i in range(len(temp))])

temp = list(temp)


for sort in temp:
    fig, ax = plt.subplots(ncols = 3, nrows=2)

    #set axes properties
    for i in range(3):
        for j in range(2):
            if j==1 and i==2:
                break
            ax[j,i].set_xlabel('wielkość tablicy', fontsize=7)
            ax[j,i].set_ylabel('czas (s)', fontsize=7) 
            ax[j,i].spines['top'].set_color(COLOR)
            ax[j,i].set_xticks([1000,10000])
            ax[j,i].spines['right'].set_color(COLOR)
            ax[j,i].spines['bottom'].set_color(COLOR)
            ax[j,i].spines['left'].set_color(COLOR)
            ax[j,i].set_facecolor(BACKGROUND)
    for i, data in enumerate(sort):

        name, x, y, std = data



        ax[i%2, i//2].errorbar(x, y, std, color = plot_colors[name], marker = '.')
        ax[i%2, i//2].set_title(GENNAMES[i])

    ax[1,2].axis('off')

    fig.suptitle(sort[0][0] + " zmienność wyników", fontsize=16)
    fig.set_facecolor(BACKGROUND)
    fig.tight_layout()
    fig.set_size_inches(10,6)
    plt.savefig(sort[0][0] + " zmienność wyników.png")


