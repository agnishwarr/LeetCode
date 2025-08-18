
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        Backtracking over all pairwise operations on floating numbers
        until one value remains that is approximately 24.
        """
        EPS = 1e-6                                   # small tolerance for float comparison

        def dfs(nums: List[float]) -> bool:
            # If only one number remains, check if it's essentially 24
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            # Try all unordered pairs i, j with i != j
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    # Build the next list excluding i and j
                    next_nums = []
                    for k in range(n):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    a, b = nums[i], nums[j]

                    # Try all operations a op b
                    # Addition
                    next_nums.append(a + b)          # a + b
                    if dfs(next_nums):
                        return True
                    next_nums.pop()

                    # Subtraction
                    next_nums.append(a - b)          # a - b
                    if dfs(next_nums):
                        return True
                    next_nums.pop()

                    # Reverse subtraction only when exploring different order
                    # Since i and j range over all ordered pairs, we already try both a-b and b-a
                    # Multiplication
                    next_nums.append(a * b)          # a * b
                    if dfs(next_nums):
                        return True
                    next_nums.pop()

                    # Division, guard divide by zero with tolerance
                    if abs(b) > EPS:
                        next_nums.append(a / b)      # a / b
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

            return False

        # Start with floats to keep real division semantics
        return dfs([float(x) for x in cards])