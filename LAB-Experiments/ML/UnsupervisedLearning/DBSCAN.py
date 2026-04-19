# DBSCAN with cluster boundary visualization

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from matplotlib.patches import Ellipse

X = np.array([
    [2, 3], [3, 3], [3, 4], [4, 5], [5, 6],   
    [8, 2], [8, 3], [9, 2],                   
    [3, 8], [4, 9], [5, 9],                   
    [11, 11]                                  
])

dbscan = DBSCAN(eps=2, min_samples=2)
labels = dbscan.fit_predict(X)

plt.figure()

unique_labels = set(labels)

for label in unique_labels:

    if label == -1:
        plt.scatter(
            X[labels == label, 0],
            X[labels == label, 1],
            s=80,
            label="Noise"
        )

    else:
        cluster_points = X[labels == label]

        plt.scatter(
            cluster_points[:, 0],
            cluster_points[:, 1],
            s=80,
            label=f"Cluster {label}"
        )

        x_center = cluster_points[:, 0].mean()
        y_center = cluster_points[:, 1].mean()

        width = (cluster_points[:, 0].max() -
                 cluster_points[:, 0].min()) + 1

        height = (cluster_points[:, 1].max() -
                  cluster_points[:, 1].min()) + 1

        ellipse = Ellipse(
            (x_center, y_center),
            width,
            height,
            fill=False
        )

        plt.gca().add_patch(ellipse)

plt.title("DBSCAN Clusters with Regions")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

plt.show()

print("Cluster Labels:", labels)
