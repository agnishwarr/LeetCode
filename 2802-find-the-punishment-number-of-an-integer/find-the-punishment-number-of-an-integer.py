class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(sq_str, target):
            def dfs(index, current_sum):
                if index == len(sq_str):
                    return current_sum == target
                for j in range(index + 1, len(sq_str) + 1):
                    part = int(sq_str[index:j])
                    if dfs(j, current_sum + part):
                        return True
                return False
            return dfs(0, 0)
        
        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if can_partition(str(sq), i):
                total += sq
        return total
