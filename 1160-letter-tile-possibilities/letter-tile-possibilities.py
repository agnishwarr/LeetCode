from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        
        def dfs(counter):
            total = 0
            for ch in counter:
                if counter[ch] > 0:
                    total += 1
                    counter[ch] -= 1
                    total += dfs(counter)
                    counter[ch] += 1
            return total
        
        return dfs(count)
