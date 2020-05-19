from sklearn.datasets import make_moons, make_circles
from sklearn.cluster import KMeans, SpectralClustering
import matplotlib.pyplot as plt


def test():
    X1 = make_circles(factor=0.5, noise=0.05, n_samples=1500)

    # Moons
    X2 = make_moons(n_samples=1500, noise=0.05)
    print(f'x1 shape is {X1[0].shape}, x2 shape is {X2[0].shape}')
    fig, ax = plt.subplots(1, 2)
    for i, X in enumerate([X1, X2]):
        fig.set_size_inches(18, 7)
        km = KMeans(n_clusters=2)
        km.fit(X[0])
        labels = km.predict(X[0])
        centroids = km.cluster_centers_

        ax[i].scatter(X[0][:, 0], X[0][:, 1], c=labels)
        ax[i].scatter(centroids[0, 0], centroids[0, 1], marker='*', s=400, c='r')
        ax[i].scatter(centroids[1, 0], centroids[1, 1], marker='+', s=300, c='green')
    plt.suptitle('Simulated data', y=1.05, fontsize=22, fontweight='semibold')
    plt.tight_layout()


def test_spectral_cluster():
    # Cricles
    X1 = make_circles(factor=0.5, noise=0.05, n_samples=1500)

    # Moons
    X2 = make_moons(n_samples=1500, noise=0.05)

    fig, ax = plt.subplots(1, 2)
    for i, X in enumerate([X1, X2]):
        fig.set_size_inches(18, 7)
        sp = SpectralClustering(n_clusters=2, affinity='nearest_neighbors')
        sp.fit(X[0])
        labels = sp.labels_
        ax[i].scatter(X[0][:, 0], X[0][:, 1], c=labels)
    plt.suptitle('Simulated data', y=1.05, fontsize=22, fontweight='semibold')
    plt.tight_layout();


if __name__ == '__main__':
    test_spectral_cluster()
