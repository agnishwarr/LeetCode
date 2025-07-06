from collections import Counter

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)
        res = -1
        for num, count in freq.items():
            if num == count:
                res = max(res, num)
        return res