import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances
import pandas as pd

def calculate_lag_score(spicepoints, centers):
    # Compute the distance matrix between all spice points and centers
    distances = pairwise_distances(spicepoints, centers)
    
    # Find the minimum distance for each spice point (nearest center)
    min_distances = np.min(distances, axis=1)
    
    # LAG score is the sum of squared minimum distances
    lag_score = np.sum(min_distances**2)
    
    return lag_score

def calculate_silhouette_score(spicepoints, centers, labels):
    N = spicepoints.shape[0]
    a = np.zeros(N)  # Intra-cluster distances
    b = np.zeros(N)  # Nearest neighbor cluster distances
    
    # Compute intra-cluster distances (a(i)) for each spice point
    for i in range(N):
        same_cluster_points = spicepoints[labels == labels[i]]
        a[i] = np.mean(np.linalg.norm(same_cluster_points - spicepoints[i], axis=1))
    
    # Compute inter-cluster distances (b(i)) for each spice point
    for i in range(N):
        distances_to_centers = np.linalg.norm(centers - spicepoints[i], axis=1)
        nearest_cluster_idx = np.argsort(distances_to_centers)[1]  # 2nd nearest cluster
        other_cluster_points = spicepoints[labels == nearest_cluster_idx]
        b[i] = np.mean(np.linalg.norm(other_cluster_points - spicepoints[i], axis=1))
    
    # Compute silhouette score
    silhouette_scores = (b - a) / np.maximum(a, b)
    
    return np.mean(silhouette_scores)

def guess_K(data_path, max_K, N_iter):
    # Load the spice points data
    spicepoints = pd.read_csv(data_path).values
    
    # Placeholder for scores
    lag_scores_default = []
    silhouette_scores_default = []
    lag_scores = []
    silhouette_scores = []
    
    # Run the algorithm for different values of K
    for K in range(2, max_K + 1):
        for _ in range(N_iter):
            # Default random initialization (You may want to replace this with actual random init.)
            centers_default = spicepoints[np.random.choice(spicepoints.shape[0], K, replace=False)]
            labels_default = np.argmin(pairwise_distances(spicepoints, centers_default), axis=1)
            lag_scores_default.append(calculate_lag_score(spicepoints, centers_default))
            silhouette_scores_default.append(calculate_silhouette_score(spicepoints, centers_default, labels_default))
            
            # Heuristic initialization
            centers_heuristic = initialise_spice_centers(spicepoints, K)  # Pre-implemented function
            labels_heuristic = np.argmin(pairwise_distances(spicepoints, centers_heuristic), axis=1)
            lag_scores.append(calculate_lag_score(spicepoints, centers_heuristic))
            silhouette_scores.append(calculate_silhouette_score(spicepoints, centers_heuristic, labels_heuristic))
    
    # Plot the results
    # LAG Scores plot
    plt.plot(range(2, max_K + 1), lag_scores_default, color='blue', label='Default Initialisation')
    plt.plot(range(2, max_K + 1), lag_scores, color='red', label='Heuristic Initialisation')
    plt.xlabel('K')
    plt.ylabel('Score')
    plt.title('LAG Scores')
    plt.legend()
    plt.savefig('LAG_scores.png')

    # Silhouette Scores plot
    plt.plot(range(2, max_K + 1), silhouette_scores_default, color='blue', label='Default Initialisation')
    plt.plot(range(2, max_K + 1), silhouette_scores, color='red', label='Heuristic Initialisation')
    plt.xlabel('K')
    plt.ylabel('Score')
    plt.title('Silhouette Scores')
    plt.legend()
    plt.savefig('SIL_scores.png')

# Example to test:
guess_K('spicepoints.csv', 6, 500)
