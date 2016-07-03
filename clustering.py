''' This file does all the heavy lifting, from a ML standpoint. '''

from sklearn.cluster import AffinityPropagation
import os
from sklearn.cluster import KMeans
import numpy as np


def fix_tier_orders(A):
    ''' Sometimes, clustering algorithms provide labels that are
    not in ascending order. This method aims to fix that. '''
    inf = min(A)
    already_swapped = [inf]
    swap(A, inf, A[0])
    inf = inf + 1
    for i in range(1, len(A)):
        if A[i] not in already_swapped:
            swap(A, inf, A[i])
            inf = inf + 1
            already_swapped.append(A[i])


def swap(A, entry, inf):
    '''a simple swap function on lists'''
    for i in range(len(A)):
        if A[i] == entry:
            A[i] = inf
        elif A[i] == inf:
            A[i] = entry
    return

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DIRECTORY = os.path.join(CURRENT_DIR, "Saved")
FILE_NAMES = os.listdir(SAVE_DIRECTORY)
LOADED_DATA = np.load(SAVE_DIRECTORY + "/" + FILE_NAMES[1])
PLAYERS = []
PLAYER_STATS = []
for row in LOADED_DATA:
    try:
        PLAYER_STATS.append([float(i) for i in row[1:]])
        PLAYERS.append(row[0])
    except:
        continue

X = np.asarray(PLAYER_STATS)

K_MEANS = KMeans(init='k-means++', n_clusters=7, n_init=10)
K_MEANS.fit(X)

# af = AffinityPropagation(preference=-50).fit(X)
TIER_LABELS = list(K_MEANS.labels_)
fix_tier_orders(TIER_LABELS)

PLAYER_TIERS = {}
for i in range(len(TIER_LABELS)):
    if TIER_LABELS[i] not in PLAYER_TIERS.keys():
        PLAYER_TIERS[TIER_LABELS[i]] = [PLAYERS[i]]
    else:
        PLAYER_TIERS[TIER_LABELS[i]].append(PLAYERS[i])
print PLAYER_TIERS
