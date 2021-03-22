#1094. Car Pooling:

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tsp = []
        #note that you may want to drop the passenger first and then add on the new passenger.
        for trip in trips:
            tsp.append([trip[1], trip[0]])
            tsp.append([trip[2], -trip[0]])
        tsp.sort(key = lambda X: (X[0], X[1]))
        capacity_usage = 0
        for time, passengerChange in tsp:
            capacity_usage += passengerChange
            if capacity_usage > capacity:
                return False
        return True
