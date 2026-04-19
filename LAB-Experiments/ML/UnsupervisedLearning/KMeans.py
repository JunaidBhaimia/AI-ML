# K-Means Clustering using store_customers.csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("store_customers.csv")

data.dropna(inplace=True)

X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

kmeans = KMeans(n_clusters=5, random_state=0)

kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("\nCentroids:")
print(centroids)

plt.scatter(X['Annual Income (k$)'],
            X['Spending Score (1-100)'],
            c=labels)

plt.scatter(centroids[:, 0],
            centroids[:, 1],
            marker='x',
            s=200)

plt.title("K-Means Clustering (Mall Customers)")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.show()
