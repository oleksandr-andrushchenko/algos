# Given a stream of integers and a window size size, compute the moving average of all integers in the sliding window.
#
# Implement the MovingAverage class:
#
# MovingAverage(int size) Initializes the object with the size of the window.
# double next(int val) Returns the moving average of the last size values in the stream.

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.window_sum += val

        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.window_sum -= removed

        return self.window_sum / len(self.queue)
