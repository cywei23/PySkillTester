



class MovingAverage():
    def __init__(self, window_size):
        self.window_size = window_size
        self.data_stream = []
        self.current_sum = 0.0
        
    def add(self, value):
        if len(self.data_stream) == self.window_size:
            self.current_sum -= self.data_stream.pop(0)
        self.data_stream.append(value)
        self.current_sum += value
        
    def get_moving_average(self):
        return self.current_sum / len(self.data_stream)