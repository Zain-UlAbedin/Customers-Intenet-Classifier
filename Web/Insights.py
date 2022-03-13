import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from palettable.colorbrewer.qualitative import Pastel1_7
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import squarify
import pickle
from django.conf import settings, os


def donutplot(complain, recommend, query, appreciation, others):

    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    Names = ['complaints', 'Recommendations', 'Queries', 'Appreciation', 'Others']
    Data = [complain, recommend, query, appreciation, others]
    explode = (0.05, 0.05, 0.05, 0.05, 0.05)
    my_Circle = plt.Circle((0, 0), 0.7, color='white')

    ax.pie(Data, labels=Names, colors=Pastel1_7.hex_colors, explode=explode, pctdistance=0.83, autopct='%1.1f%%')
    ax.legend()
    ax.add_artist(my_Circle)

    return fig


def BarGraph(complain, recommend, query, appreciation, others):
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    height = [complain, recommend, query, appreciation, others]
    bars = ['complaints', 'Recommendations', 'Queries', 'Appreciation', 'Others']
    y_pos = [0, 2, 4, 6, 8]

    total_reviews = str(complain + others + recommend + query + appreciation)

    ax.bar(y_pos, height, color=Pastel1_7.hex_colors, edgecolor='white', align='center', label="Total Reviews are :" + total_reviews)

    ax.set_xlabel("Categories")
    ax.set_ylabel("# of Reviews")

    ax.set_xticks(y_pos)
    ax.set_xticklabels(bars)
    for i in range(len(bars)):
        ax.text(x=y_pos[i] - .3, y=height[i], s=height[i], size=12.5)

    return fig


# Tree Map figure
def TreeMap(File_name, Data):
    # If you have 2 lists
    #fig = Figure()
    #ax = fig.add_subplot(1, 1, 1)
    ax = squarify.plot(sizes=Data, label=File_name, alpha=.7)

    return ax


def MultiBargraph():

    barWidth = 0.25

    # set height of bar
    bars1 = [12, 30, 1, 8, 22]
    bars2 = [28, 6, 16, 5, 10]
    bars3 = [29, 3, 24, 25, 17]

    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='var1')
    plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='var2')
    plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')

    # Add xticks on the middle of the group bars
    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])

    # Create legend & Show graphic
    plt.legend()
    plt.show()


def WordCloud(Name):
    File_Stored_loc = settings.MEDIA_ROOT + '\static\Files/'
    Name = Name.replace('.xlsx', '')
    file = open(File_Stored_loc + Name + "1" + ".txt", 'rb')
    Pdata = pickle.load(file)

    fig = Figure(figsize=(8, 8), facecolor=None)
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(Pdata['WordCloud'])
    ax.axis('off')
    # ax.xaxis.set_visible(False)
    # ax.yaxis.set_visible(False)
    fig.tight_layout(pad=0)
    return fig
