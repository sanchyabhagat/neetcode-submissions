class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # Negative since python only has minHeap 
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        time = 0
        # queue to check when the task can be added back based on current time + n
        # same ple value [taskCount remaining, currentTime + n (idle time between same tasks)]
        q = deque()

        while q or maxHeap:
            time += 1

            if maxHeap:
                currentCount = heapq.heappop(maxHeap)
                # Do the task once
                currentCount += 1
                # Add this task back to the queue, if non-zero
                if currentCount:
                    q.append([currentCount, time+n])
                
            # Check if new task at top is ready and if q is valid
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
        