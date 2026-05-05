class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O[n log(k)]
        count = defaultdict()
        minHeap = []
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, freq in count.items():
            heapq.heappush(minHeap, [freq, n])

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        
        return res
        