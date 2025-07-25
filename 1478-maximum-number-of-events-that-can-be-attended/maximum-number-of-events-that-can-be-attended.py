import heapq

class Solution:
    def maxEvents(self, events):
        events.sort()
        min_heap = []
        i = 0
        n = len(events)
        day = 0
        res = 0

        while i < n or min_heap:
            if not min_heap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                res += 1
                day += 1
        return res
