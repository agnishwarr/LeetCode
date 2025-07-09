class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        durations = [endTime[i] - startTime[i] for i in range(n)]
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + durations[i]

        max_gap = 0
        for i in range(n - k + 1):
            left = endTime[i - 1] if i > 0 else 0
            right = startTime[i + k] if i + k < n else eventTime
            total_dur = prefix_sum[i + k] - prefix_sum[i]
            max_gap = max(max_gap, right - left - total_dur)

        return max_gap
