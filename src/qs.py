q1 = """
As a Senior Data Scientist, you have been tasked with creating an efficient algorithm to calculate the moving average of a data stream. The moving average should be calculated using a fixed window size.
Create a Python class called MovingAverage, with the following methods:

1. __init__(self, window_size: int): Initializes a new MovingAverage object with a specified window size.
2. add(self, value: float) -> None: Adds a new value to the data stream.
3. get_moving_average(self) -> float: Returns the current moving average of the data stream considering the last window_size values. If there are fewer than window_size values in the data stream, return the average of all available values.

Example:
python
Copy code

moving_average = MovingAverage(3)
moving_average.add(1)print(moving_average.get_moving_average())  # Output: 1.0

moving_average.add(2)print(moving_average.get_moving_average())  # Output: 1.5

moving_average.add(3)print(moving_average.get_moving_average())  # Output: 2.0

moving_average.add(4)print(moving_average.get_moving_average())  # Output: 3.0


Good luck!

Test code: 
moving_average = MovingAverage(3)
moving_average.add(1)
print(moving_average.get_moving_average())
"""

q2 = """
Question:

Given a list of integer intervals, merge any overlapping intervals and return the resulting list of non-overlapping intervals. The input list will be unsorted, and the output list should be sorted based on the intervals' start times.

Example:

python
Copy code
Input: intervals = [(1, 5), (8, 10), (2, 6), (15, 18), (10, 12)]
Output: [(1, 6), (8, 12), (15, 18)]
Explanation:

The intervals (1, 5) and (2, 6) overlap, so they are merged into (1, 6).
The intervals (8, 10) and (10, 12) overlap, so they are merged into (8, 12).
The interval (15, 18) does not overlap with any other intervals, so it remains unchanged.

Your task is to write a Python function to perform the merging of overlapping intervals:

python
Copy code
def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # Your implementation here
This question tests your ability to work with lists, tuples, and sorting algorithms, as well as your understanding of interval manipulation and algorithmic problem-solving.
"""


q3 = """
You are given a dataset containing information about houses and their sale prices. The dataset has the following features: number of bedrooms, number of bathrooms, square footage, and sale price. The dataset is represented as a list of dictionaries, where each dictionary contains the features of a single house.
Your task is to write a Python function to calculate the Pearson correlation coefficient between the number of bedrooms and the sale price. The Pearson correlation coefficient measures the linear relationship between two datasets. The value of the coefficient ranges from -1 (perfect negative correlation) to 1 (perfect positive correlation). A value of 0 indicates no correlation.
python
Copy code

def pearson_correlation_coefficient(houses: List[Dict[str, float]]) -> float:
    # Your implementation here


Example:
python
Copy code

houses = [
    {"bedrooms": 2, "bathrooms": 1, "square_footage": 800, "price": 250000},
    {"bedrooms": 3, "bathrooms": 2, "square_footage": 1200, "price": 350000},
    {"bedrooms": 4, "bathrooms": 3, "square_footage": 2000, "price": 500000},
    {"bedrooms": 5, "bathrooms": 4, "square_footage": 3000, "price": 750000},
]

output = pearson_correlation_coefficient(houses)print(output)  # Should be close to 1, as there is a st
"""


q4 = """
Question:

Implement the k-Nearest Neighbors (kNN) algorithm from scratch in Python, given a dataset and a new data point. The algorithm should find the k-nearest neighbors to the new data point in the dataset and return their labels. You can use Euclidean distance as a distance metric.

Input:

dataset: A list of tuples, where each tuple consists of a feature vector and a label. The feature vector is represented as a list of floats, and the label is a string.
new_point: A feature vector represented as a list of floats.
k: The number of nearest neighbors to consider (an integer).
Output:

A list of labels of the k-nearest neighbors to the new data point.
Example:

python
Copy code
dataset = [
    ([1.0, 2.0], 'A'),
    ([2.0, 3.0], 'B'),
    ([3.0, 4.0], 'A'),
    ([4.0, 5.0], 'B'),
    ([5.0, 6.0], 'A')
]

new_point = [2.5, 3.5]
k = 3

result = knn_algorithm(dataset, new_point, k)
print(result)  # Output: ['A', 'B', 'A']
"""


q5 = """
Question:

Implement the k-Means clustering algorithm from scratch in Python. Given a dataset and the number of clusters, the algorithm should group the data points into clusters based on their similarity. You can use Euclidean distance as a distance metric.

Input:

dataset: A list of feature vectors, where each feature vector is represented as a list of floats.
k: The number of clusters to form (an integer).
max_iterations: The maximum number of iterations to perform (an integer, optional; default is 100).
Output:

A list of cluster assignments, where each assignment is an integer from 0 to k-1, representing the cluster number for each data point.
Example:

python
Copy code
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

Note that the k-Means clustering algorithm is sensitive to the initial centroids' placement, so multiple runs may produce different results. In this example, the expected output is a list of cluster assignments, but the exact assignments may vary due to the randomness of centroid initialization. You can use this prompt as a starting point for your implementation. Good luck with your interview preparation!
"""

