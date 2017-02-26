import matplotlib.pyplot as plt
import numpy as np
from findClosestCentroids import findClosestCentroids
from computeCentroids import computeCentroids


def plotDataPoint(X, idx, K):
    plt.scatter(X[:, 0], X[:, 1])
#     plt.show()


def drawLine(p1, p2):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]])
#     plt.show()


def plotProgresskMeans(X, centroids, previous, idx, K, i):
    #     plotDataPoint(X, idx, K)
    #     plt.plot(centroids[:, 0], centroids[:, 1])
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='+', c='r')
    for j in range(np.size(centroids, axis=0)):
        drawLine(centroids[j, :], previous[j, :])
#     plt.show()


def runkMeans(X, initial_centroids, max_iters, plot_progress):
    m, n = np.shape(X)
    K = np.size(initial_centroids, axis=0)
    centroids = initial_centroids
    previous_centroids = centroids
    idx = np.zeros((m, 1))
    if plot_progress:
        plotDataPoint(X, idx, K)
    for i in range(max_iters):
        idx = findClosestCentroids(X, centroids)
        if plot_progress:
            plotProgresskMeans(X, centroids, previous_centroids, idx, K, i)
            previous_centroids = centroids
        centroids = computeCentroids(X, idx, K)
    plt.show()
    return centroids, idx
