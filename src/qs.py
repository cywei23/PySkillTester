q1 = (
    "As a Senior Data Scientist, you have been tasked with creating an efficient algorithm to calculate the moving average of a data stream. The moving average should be calculated using a fixed window size.\n"
    "Create a Python class called MovingAverage, with the following methods:\n\n"
    "1. __init__(self, window_size: int): Initializes a new MovingAverage object with a specified window size.\n"
    "2. add(self, value: float) -> None: Adds a new value to the data stream.\n"
    "3. get_moving_average(self) -> float: Returns the current moving average of the data stream considering the last window_size values. If there are fewer than window_size values in the data stream, return the average of all available values.\n\n"
    "Example:\n\n"
    "moving_average = MovingAverage(3)\n"
    "moving_average.add(1)\n"
    "print(moving_average.get_moving_average())  # Output: 1.0\n\n"
    "moving_average.add(2)\n"
    "print(moving_average.get_moving_average())  # Output: 1.5\n\n"
    "moving_average.add(3)\n"
    "print(moving_average.get_moving_average())  # Output: 2.0\n\n"
    "moving_average.add(4)\n"
    "print(moving_average.get_moving_average())  # Output: 3.0\n\n"
    "Good luck!\n\n"
    "Test code:\n"
    "moving_average = MovingAverage(3)\n"
    "moving_average.add(1)\n"
    "print(moving_average.get_moving_average())"
)


q2 = (
    "Given a list of integer intervals, merge any overlapping intervals and return the resulting list of non-overlapping intervals. The input list will be unsorted, and the output list should be sorted based on the intervals' start times.\n\n"
    "Example:\n\n"
    "Input: intervals = [(1, 5), (8, 10), (2, 6), (15, 18), (10, 12)]\n"
    "Output: [(1, 6), (8, 12), (15, 18)]\n\n"
    "Explanation:\n"
    "The intervals (1, 5) and (2, 6) overlap, so they are merged into (1, 6). The intervals (8, 10) and (10, 12) overlap, so they are merged into (8, 12). The interval (15, 18) does not overlap with any other intervals, so it remains unchanged.\n"
    "Your task is to write a Python function to perform the merging of overlapping intervals:\n\n"
    "def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:\n"
    "    # Your implementation here\n\n"
    "Test codes:\n"
    "intervals = [(1, 5), (8, 10), (2, 6), (15, 18), (10, 12)]\n"
    "print(merge_intervals(intervals)) # Output: [(1, 6), (8, 12), (15, 18)]"
)


q3 = (
    "You are given a dataset containing information about houses and their sale prices. The dataset has the following features: number of bedrooms, number of bathrooms, square footage, and sale price. The dataset is represented as a list of dictionaries, where each dictionary contains the features of a single house.\n\n"
    "Your task is to write a Python function to calculate the Pearson correlation coefficient between the number of bedrooms and the sale price. The Pearson correlation coefficient measures the linear relationship between two datasets. The value of the coefficient ranges from -1 (perfect negative correlation) to 1 (perfect positive correlation). A value of 0 indicates no correlation.\n\n"
    "def pearson_correlation_coefficient(houses: List[Dict[str, float]]) -> float:\n"
    "    # Your implementation here\n\n"
    "Example:\n\n"
    "houses = [\n"
    "    {\"bedrooms\": 2, \"bathrooms\": 1, \"square_footage\": 800, \"price\": 250000},\n"
    "    {\"bedrooms\": 3, \"bathrooms\": 2, \"square_footage\": 1200, \"price\": 350000},\n"
    "    {\"bedrooms\": 4, \"bathrooms\": 3, \"square_footage\": 2000, \"price\": 500000},\n"
    "    {\"bedrooms\": 5, \"bathrooms\": 4, \"square_footage\": 3000, \"price\": 750000},\n"
    "]\n\n"
    "output = pearson_correlation_coefficient(houses)\n"
    "print(output)  # Should be close to 1, as there is a strong positive correlation\n"
)

