class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        all = 0

        for x in nums:
            all |= x
            
        return all << (len(nums) - 1)