class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # add to small by default, -1 * since we want max heap
        heapq.heappush(self.small, num * -1)

        # check if small[0] > large[0], i.e. wrong order
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        
        # size imbalance
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2 
        