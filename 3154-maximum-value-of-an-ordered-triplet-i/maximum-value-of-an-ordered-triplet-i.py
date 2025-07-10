class Solution:
    def maximumTripletValue(self, nums):
        n = len(nums)
        max_value = 0
        for j in range(1, n - 1):
            max_i = max(nums[:j])
            for k in range(j + 1, n):
                value = (max_i - nums[j]) * nums[k]
                if value > max_value:
                    max_value = value
        return max_value
