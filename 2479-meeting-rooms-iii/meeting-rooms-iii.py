import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()  
        
        available = list(range(n))  
        heapq.heapify(available)
        
        occupied = []  
        count = [0] * n
        
        for start, end in meetings:

            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                end_time, room = heapq.heappop(occupied)
                duration = end - start
                new_end = end_time + duration
                heapq.heappush(occupied, (new_end, room))
            
            count[room] += 1
        
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
