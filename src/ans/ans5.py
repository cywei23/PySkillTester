import random

def euclidean_distance(point1, point2):
    return sum((a-b)**2 for a, b in zip(point1, point2)) ** 0.5

def mean_point(points):
    return [sum(point) / len(points) for point in zip(*points)]

def k_means_clustering(dataset, k, max_iteration=10):
    # initialize centroid by randomly selecting k data points from dataset
    centroids = random.sample(dataset, k)
    
    for _ in range(max_iteration):
        # assign each data point to the nearest centroid
        clusters = [[] for _ in range(k)]
        for point in dataset:
            closest_centroid_index = min(range(k), key=lambda i: euclidean_distance(point, centroids[i]))
            clusters[closest_centroid_index].append(point)
        
        # update centroid point by calculating the mean of all data points in each clusters
        new_centroids = [mean_point(cluster) for cluster in clusters]
        
        if new_centroids == centroids:
            break
        
        centroids = new_centroids
        
    # assign final cluster indices to the data points
    cluster_assignments = [min(range(k), key=lambda i: euclidean_distance(point, centroids[i])) for point in dataset]
    
    return cluster_assignments



# Example usage
dataset = [
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0],
    [4.0, 5.0],
    [5.0, 6.0]
]

k = 2
max_iterations = 100

result = k_means_clustering(dataset, k, max_iterations)
print(result)  # Output: [0, 0, 1, 1, 1] (or any similar clustering)
