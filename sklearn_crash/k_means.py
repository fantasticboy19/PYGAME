import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import numpy as np



data, target = make_blobs(
    n_samples=200,
    n_features=2,
    centers=3,
    cluster_std=.5,
    random_state=0,
    shuffle=True
)

# km = KMeans(n_clusters=4, init='random',
#     n_init=10, max_iter=300,
#     tol=1e-04, random_state=0)
# y_km = km.fit_predict(data)


# fig, axes = plt.subplots(1, 2, sharey=True)
#
# axes = axes.flatten()
# axes[0].scatter(data[:, 0], data[:, 1], c=target)
#
# axes[1].scatter(
#     data[y_km == 0, 0], data[y_km == 0, 1],
#     s=50, c='lightgreen',
#     marker='s', edgecolor='black',
#     label='cluster 1'
# )
#
# axes[1].scatter(
#     data[y_km == 1, 0], data[y_km == 1, 1],
#     s=50, c='orange',
#     marker='o', edgecolor='black',
#     label='cluster 2'
# )
#
# axes[1].scatter(
#     data[y_km == 2, 0], data[y_km == 2, 1],
#     s=50, c='lightblue',
#     marker='v', edgecolor='black',
#     label='cluster 3'
# )
# axes[1].scatter(
#     data[y_km == 3, 0], data[y_km == 3, 1],
#     s=50, c='blue',
#     marker='v', edgecolor='black',
#     label='cluster 4'
# )

# calculate distortion for a range of number of cluster
distortions = []
for i in range(1, 11):
    km = KMeans(
        n_clusters=i, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=0
    )
    km.fit(data)
    distortions.append(km.inertia_)

# plot

plt.plot(range(1, 11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()
