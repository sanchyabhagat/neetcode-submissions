"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        minHeap = [] # this will have minimum end times 

        intervals.sort(key=lambda x:x.start)

        for interval in intervals:
            if minHeap and interval.start >= minHeap[0]:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, interval.end)
        
        return len(minHeap) <= 1
