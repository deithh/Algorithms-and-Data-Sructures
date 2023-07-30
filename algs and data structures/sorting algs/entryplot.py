import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from datagen import Data
        
#set font color
COLOR = 'white'
mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR



values = (0,100,100)

#colormap for plot
cmap = plt.get_cmap("inferno")
rescale = lambda y: (y - np.min(y)) / (np.max(y) - np.min(y))

#make grid
fig, ax = plt.subplots(ncols = 3, nrows=2)

#set axes properties
for i in range(3):
    for j in range(2):
        if j==1 and i==2:
            break
        ax[j,i].set_xlabel('indeks', fontsize=7)
        ax[j,i].set_ylabel('wartość', fontsize=7) 
        ax[j,i].set_xticks([])
        ax[j,i].set_yticks([])
        ax[j,i].spines['top'].set_color("white")
        ax[j,i].spines['right'].set_color("white")
        ax[j,i].spines['bottom'].set_color("white")
        ax[j,i].spines['left'].set_color("white")
        ax[j,i].set_facecolor("black")

#set axes
d = Data.noise(*values)
ax[0,0].bar(range(len(d)), d, color = cmap(rescale(d)))
ax[0,0].set_title('Szum')

d = Data.up(*values)
ax[0,1].bar(range(len(d)), d, color = cmap(rescale(d)))
ax[0,1].set_title('Ciąg rosnący')

d = Data.down(*values)
ax[0,2].bar(range(len(d)), d, color = cmap(rescale(d)))
ax[0,2].set_title('Ciąg malejący')

d = Data.A(*values)
ax[1,0].bar(range(len(d)), d, color = cmap(rescale(d)))
ax[1,0].set_title('Ciąg A-kształtny')

d = Data.const(*values)
ax[1,1].bar(range(len(d)), d, color = cmap(d[0]/values[-1]))
ax[1,1].set_title('Ciąg stały')
ax[1,1].set_ylim((0,100))

ax[1,2].axis('off')

#set figure properties
fig.suptitle('Dane wejściowe', fontsize=16)
fig.set_facecolor("black")
fig.tight_layout()
fig.set_size_inches(10, 6)
fig.savefig('inputs.png')