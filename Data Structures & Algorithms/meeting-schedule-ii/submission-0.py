"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mheap = []
        intervals.sort(key=lambda x:x.start)

        for interval in intervals:
            if mheap and interval.start >= mheap[0]:
                heapq.heappop(mheap)

            heapq.heappush(mheap, interval.end)

        return len(mheap) 