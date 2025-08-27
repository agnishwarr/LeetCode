

from typing import List, Tuple, Dict

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        n, m = len(grid), len(grid[0]) if grid else 0

        def inside(r: int, c: int) -> bool:
            return 0 <= r < n and 0 <= c < m

        memo: Dict[Tuple[int, int, int, int, int], int] = {}
        
        def dfs(r: int, c: int, k: int, expect: int, allow: int) -> int:


            if not inside(r, c) or grid[r][c] != expect:
                return 0
            
            state = (r, c, k, expect, allow)
            if state in memo:
                return memo[state]

            next_expect = 0 if expect == 2 else 2

            dr, dc = dirs[k]
            r1, c1 = r + dr, c + dc
            best = 1 + dfs(r1, c1, k, next_expect, allow)

            if allow:
                k2 = (k + 1) % 4                      
                dr2, dc2 = dirs[k2]
                r2, c2 = r + dr2, c + dc2
                best = max(best, 1 + dfs(r2, c2, k2, next_expect, 0))
            
            memo[state] = best
            return best
        
        ans = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] != 1:
                    continue
                for k in range(4):
                    dr, dc = dirs[k]
                    nr, nc = r + dr, c + dc
                    
                    tail = dfs(nr, nc, k, 2, 1)
                    ans = max(ans, 1 + tail)
        
        return ans