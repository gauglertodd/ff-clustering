# ff-clustering
Fetches EC rankings from fantasypros.com, creates tier-based rankings with ML clustering algorithms for drafting. 

The following are algorithms currently used in the making of tier-diagrams:
"Affinity-Propagation", "K-means", "Mini-Batch-Kmeans", "Meanshift", "Spectral-Clustering", "Agglomerative Clustering","DBSCAN", "Birch".

Documentation for these algorithms can be found somewhere on this page: http://scikit-learn.org/stable/modules/clustering.html#
Note that I've done very little tweaking, and have only fine-tuned the algorithms for personal use. If you want something special, you'll welcome to go ahead and change something in the "algorithms" list found in ff-clustering.py. 

I suppose that the methodolgy behind setting up the data for use with the sklearn modules is a little strange - I think these scripts download data, convert it to a np matrix, save it, take that np matrix and play with it, then save it into a slightly different np matrix without strings. A thought was, that I might someday use the unadulterated numpy matrix with all of the data in it somehow, and since the entire script only takes like 30 seconds to run, I didn't fuss about runtime issues very much. Perhaps I'll find a use for that matrix someday, but not at the moment. 

Some next steps might be as follows: 
1) Find underrated players agreed upon by an esemble of clustering algorithms
2) Build some kind of drafting system, that would suggest a player to draft based on previous picks
3) Fix the awful printouts. Make them readble, and therefore, mildly useful. 

