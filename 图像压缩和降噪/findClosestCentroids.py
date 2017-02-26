import numpy as np


def findClosestCentroids(X, centroids):
    K = np.size(centroids, axis=0)
    idx = np.zeros((np.size(X, axis=0), 1))

    for i in range(np.size(X, axis=0)):
        x = X[i, :]
        norms = np.zeros((K, 1))
        for centroid_i in range(K):
            norms[centroid_i] = (x - centroids[centroid_i, :])\
                .dot((x - centroids[centroid_i, :]).T)
        idx[i] = np.argmin(norms, axis=0)

    return idx
