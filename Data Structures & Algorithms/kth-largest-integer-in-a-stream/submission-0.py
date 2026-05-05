class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        # Python way to make heap from list, maintains the smallest element of size of k heap at top
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # check for overflow > k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # return top element which is the k largest
        return self.minHeap[0]
        
