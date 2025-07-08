from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        events.sort(key=lambda x: x[1])
        n = len(events)
        ends = [event[1] for event in events]

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            s, e, v = events[i - 1]
            j = bisect_right(ends, s - 1)
            for t in range(1, k + 1):
                dp[i][t] = max(dp[i - 1][t], dp[j][t - 1] + v)

        return max(dp[n])
