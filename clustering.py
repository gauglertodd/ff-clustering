''' This file does all the heavy lifting, from a ML standpoint. '''

from sklearn.cluster import AffinityPropagation
import os
from sklearn.cluster import KMeans
import numpy as np


def fix_tier_orders(A):
    ''' Sometimes, clustering algorithms provide labels that are
    not in ascending order. This method aims to fix that. '''
    inf = min(A)
    print inf
    already_swapped = []
    for entry in A:
        if entry not in already_swapped and entry > inf:
            swap(A, entry, inf)
            already_swapped.append(entry)
            inf = inf + 1
        elif entry == inf:
            already_swapped.append(inf)

    return A


def swap(A, entry, inf):
    '''a simple swap function on lists'''
    for i in range(len(A)):
        if A[i] == entry:
            A[i] = inf
        elif A[i] == inf:
            A[i] = entry
    return

SAVE_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "Saved")
FILE_NAMES = os.listdir(SAVE_DIRECTORY)
x = np.load(SAVE_DIRECTORY + "/" + FILE_NAMES[1])
players = []
player_stats = []
for row in x:
    try:
        player_stats.append([float(i) for i in row[1:]])
        players.append(row[0])
    except:
        continue

X = np.asarray(player_stats)

k_means = KMeans(init='k-means++', n_clusters=10, n_init=10)
k_means.fit(X)

# af = AffinityPropagation(preference=-50).fit(X)
A= list(k_means.labels_)
print A
fix_tier_orders(A)
print A
# print af.labels_

