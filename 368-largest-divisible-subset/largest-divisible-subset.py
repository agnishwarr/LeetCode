from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:                         # handle empty input
            return []
        nums.sort()                          # sorting ensures divisibility checks in increasing order
        n = len(nums)
        dp = [1] * n                         # each number alone forms length 1 subset
        prev = [-1] * n                      # to reconstruct the subset
        best_len = 1                         # track best length seen
        best_idx = 0                         # and its ending index

        # O(n^2) DP over sorted array
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:   # valid chain extension
                    if dp[j] + 1 > dp[i]:    # take longer option
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > best_len:             # update global best
                best_len = dp[i]
                best_idx = i

        # Reconstruct subset from prev pointers
        ans = []
        k = best_idx
        while k != -1:
            ans.append(nums[k])
            k = prev[k]
        ans.reverse()                        # restore increasing order
        return ans