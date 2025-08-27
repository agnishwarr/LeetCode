class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        bestdiag = -1
        bestarea = 0

        for l,w in dimensions:
            diag = l * l + w * w
            area = l * w
        
            if diag > bestdiag:
                bestdiag = diag
                bestarea = area
            elif diag == bestdiag and area > bestarea:
                bestarea = area
        return bestarea