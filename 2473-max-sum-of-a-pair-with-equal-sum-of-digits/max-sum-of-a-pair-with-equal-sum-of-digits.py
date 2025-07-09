class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        
        digit_map = defaultdict(list)
        max_sum = -1
        
        for num in nums:
            dsum = digit_sum(num)
            digit_map[dsum].append(num)
        
        for group in digit_map.values():
            if len(group) >= 2:
                group.sort(reverse=True)
                max_sum = max(max_sum, group[0] + group[1])
        
        return max_sum
