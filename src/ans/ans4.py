from collections import Counter

def euclidean_distance(point1, point2):
    return sum((a - b)**2 for a, b in zip(point1, point2)) ** 0.5

def knn_algorithm(dataset, new_point, k):
    distances = [(euclidean_distance(data_point[0], new_point), data_point[1]) for data_point in dataset]
    sorted_distances = sorted(distances, key=lambda x: x[0])
    k_nearest = sorted_distances[:k]
    k_nearest_label = [label for _, label in k_nearest]
    majority_label = Counter(k_nearest_label).most_common(1)[0][0]
    return majority_label

# Example usage
skill_tester = PySkillTester()
skill_tester.display_question()