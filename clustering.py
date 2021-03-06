''' This file does all the heavy lifting, from a ML standpoint. '''

# Scheme for UPDATED_PLAYER_SCORES:
# 0: Name
# 1: Best Rank
# 2: Worst Rank
# 3: Avg Rank
# 4: Std Dev
# 5: ADP
# 6: Tier
# 7: Overall Rank
# 8: Descending Rank (for graph purposes)
# 9: Heat Rank

import os
import sys
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def ensure_dir(name):
    '''Simple function to create directories
    in the case where they do not already exist'''
    if not os.path.exists(name):
        os.makedirs(name)


def fix_tier_orders(cluster_labels):
    ''' Sometimes, clustering algorithms provide labels that are
    not in ascending order. This method aims to fix that. '''
    inf = min(cluster_labels)
    already_swapped = [inf]
    swap(cluster_labels, inf, cluster_labels[0])
    inf = inf + 1
    for i in range(1, len(cluster_labels)):
        if cluster_labels[i] not in already_swapped:
            swap(cluster_labels, inf, cluster_labels[i])
            inf = inf + 1
            already_swapped.append(cluster_labels[i])


def swap(cluster_labels, entry, inf):
    '''a simple swap function on lists'''
    for i in range(len(cluster_labels)):
        if cluster_labels[i] == entry:
            cluster_labels[i] = inf
        elif cluster_labels[i] == inf:
            cluster_labels[i] = entry
    return


def generate_cheatsheets(NAME="K_Means",
                         ALGORITHM=KMeans(init='k-means++',
                                          n_clusters=7,
                                          n_init=10)):
    '''In theory, this should just save tons of pdfs generated from a
    user-input choice in clustering algorithm.'''
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    SAVE_DIRECTORY = os.path.join(CURRENT_DIR, "Saved")
    FILE_NAMES = os.listdir(SAVE_DIRECTORY)
    for COUNT in range(1, len(FILE_NAMES)):
        try:
            LOADED_DATA = np.load(SAVE_DIRECTORY + "/" + FILE_NAMES[COUNT])
            PLAYERS = []
            PLAYER_STATS = []
            for row in LOADED_DATA:
                try:
                    PLAYER_STATS.append([float(i) for i in row[1:]])
                    PLAYERS.append(row[0])
                except:
                    continue

            X = np.asarray(PLAYER_STATS)
            ALGORITHM.fit(X)
            TIER_LABELS = list(ALGORITHM.labels_)
            fix_tier_orders(TIER_LABELS)

            PLAYER_TIERS = {}
            for i in range(len(TIER_LABELS)):
                if TIER_LABELS[i] not in PLAYER_TIERS.keys():
                    PLAYER_TIERS[TIER_LABELS[i]] = [PLAYERS[i]]
                else:
                    PLAYER_TIERS[TIER_LABELS[i]].append(PLAYERS[i])

            CLUSTER_NUMBER = len(PLAYER_TIERS.keys())
            UPDATED_PLAYER_SCORES = []
            TOTAL_PLAYERS = len(PLAYERS)
            for i in range(TOTAL_PLAYERS):
                UPDATED_PLAYER_SCORES.append([PLAYERS[i]] +
                                             PLAYER_STATS[i] +
                                             [TIER_LABELS[i]] +
                                             [i] +
                                             [TOTAL_PLAYERS - i])

            ORDER = range(1, TOTAL_PLAYERS + 1)
            DESCENDING_RANK = [i[8] for i in UPDATED_PLAYER_SCORES]
            CLUSTER_COLORS = sns.xkcd_rgb.keys()[1:CLUSTER_NUMBER+1]

            plt.axis([0, TOTAL_PLAYERS, 0, TOTAL_PLAYERS])
            plt.rc("font", size=2)
            for i in range(len(UPDATED_PLAYER_SCORES)):
                plt.text(ORDER[i], DESCENDING_RANK[i], UPDATED_PLAYER_SCORES[i][0],
                         color=sns.xkcd_rgb[CLUSTER_COLORS[UPDATED_PLAYER_SCORES[i][6]]])
            ensure_dir(NAME)
            #plt.set_size_inches(12,12)
            plt.savefig(NAME + "/" + FILE_NAMES[COUNT][:-4] + '.pdf')
            plt.clf()
            plt.close()

        except Exception, e: print str(e)
          #  print "Unexpected error:", sys.exc_info()[0]

generate_cheatsheets()
