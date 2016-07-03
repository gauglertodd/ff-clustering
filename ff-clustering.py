''' This file offers a selection of clustering algorithms, and calls upon the
other scripts in order to generate tier diagrams of fantasy football players'''


from clustering import generate_cheatsheets
from fix_data import save_rankings
from get_rankings import get_ranks
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import MeanShift
from sklearn import cluster


def main():
    '''docstring'''
    names = [#"Affinity-Propagation",
             #"K-means",
             #"Mini-Batch-Kmeans",
             #"Meanshift",
             #"Spectral-Clustering"        ]

    algorithms = [#AffinityPropagation(preference=-50),
                  #KMeans(init='k-means++', n_clusters=7, n_init=10),
                   #MiniBatchKMeans(n_clusters=7, batch_size=200, random_state=0),
                   #MeanShift(),
                   #cluster.SpectralClustering(n_clusters=6, eigen_solver='arpack',affinity="nearest_neighbors")]




    # print "Getting rankings...."
    # get_ranks(True)
    # get_ranks(False)
    # print "Done. Saving rankings..."
    # save_rankings()
    # print "Done. Clustering...."
    #generate_cheatsheets("Affinity-Propagation", AffinityPropagation(preference=-50))
    for name, alg in zip(names, algorithms):
        print "Generating cheatsheet with the {0} algorithm".format(name)
        generate_cheatsheets(name, alg)
    print "Done"


main()
