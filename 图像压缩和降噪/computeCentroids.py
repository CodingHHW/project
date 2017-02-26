# coding: utf=8
import numpy as np


def computeCentroids(X, idx, K):
    m, n = np.shape(X)
    centroids = np.zeros((K, n))

    for i in range(K):
        pos_i, pos_j = np.where(idx == i)  # where 返回行的索引和列的索引，返回二维元祖
        centroids[i, :] = np.mean(X[pos_i, :], axis=0)
    return centroids
