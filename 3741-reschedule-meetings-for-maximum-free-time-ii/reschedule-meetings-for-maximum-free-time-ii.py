from typing import List

class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)  
        max_free_time = 0  

        left_gaps = [0] * n
        left_gaps[0] = startTime[0]  
        for i in range(1, n):
            left_gaps[i] = max(left_gaps[i - 1], startTime[i] - endTime[i - 1])
      
        
        right_gaps = [0] * n
        right_gaps[n - 1] = eventTime - endTime[-1] 
        for i in range(n - 2, -1, -1):
            right_gaps[i] = max(right_gaps[i + 1], startTime[i + 1] - endTime[i])
    
        for i in range(n):
           
            left_gap = left_gaps[i] if i == 0 else startTime[i] - endTime[i - 1]
            right_gap = right_gaps[i] if i == n - 1 else startTime[i + 1] - endTime[i]
          
            interval = 0
            if (
                i != 0
                and left_gaps[i - 1] >= (endTime[i] - startTime[i])
                or i != n - 1
                and right_gaps[i + 1] >= (endTime[i] - startTime[i])
            ):
                interval = endTime[i] - startTime[i]

            max_free_time = max(max_free_time, left_gap + interval + right_gap)
      
        return max_free_time