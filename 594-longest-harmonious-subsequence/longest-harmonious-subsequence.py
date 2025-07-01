class Solution(object):
    def findLHS(self, nums):
        count = Counter(nums)
        max_len=0

        for num in count:
            if num+1 in count:
                max_len = max(max_len, count[num]+count[num+1])
        return max_len