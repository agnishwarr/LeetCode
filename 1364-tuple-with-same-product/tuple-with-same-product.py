from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product_map = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1

        total = 0
        for count in product_map.values():
            if count > 1:
                total += count * (count - 1) * 4

        return total
