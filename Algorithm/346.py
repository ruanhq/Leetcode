#346. Moving average from data stream:
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.list = []
    #returns the moving average of the last size values of the stream.
    def next(self, val: int) -> float:
        currentSize = self.size
        currentList = self.list
        currentList.append(val)
        windowSum = sum(currentList[-currentSize:])
        return windowSum/ min(self.size, len(currentList))


class MovingAverage:
    def __init__(self, size: int):
        self.size = size 
        self.list = []

    def next(self, val: int) -> float:
        currentSize = self.size
        currentList = self.list
        currentList.append(val)
        windowSum = sum(currentList[-currentSize:])
        return windowSum/ min(self.size, len(currentList))












