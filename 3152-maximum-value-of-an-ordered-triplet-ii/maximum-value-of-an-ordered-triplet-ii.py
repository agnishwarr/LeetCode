class Solution:
    def maximumTripletValue(self, nums):
        n = len(nums)
        max_left = [0] * n
        max_left[0] = nums[0]
        
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])
        
        result = 0
        max_k = nums[-1]

        for j in range(n - 2, 0, -1):
            max_k = max(max_k, nums[j + 1])
            diff = max_left[j - 1] - nums[j]
            if diff > 0:
                result = max(result, diff * max_k)
        
        return result
