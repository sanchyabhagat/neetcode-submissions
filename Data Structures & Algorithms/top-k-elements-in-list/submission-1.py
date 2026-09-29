class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count each elements
        # keep adding to minHeap [frq, element]
        # pop if size of heap > k
        # at the end we get k top elemenents in the heap

        counts = Counter(nums)
        minHeap = []
        res = []

        for item, count in counts.items():
            heapq.heappush(minHeap, (count, item))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        
        return res
            
        