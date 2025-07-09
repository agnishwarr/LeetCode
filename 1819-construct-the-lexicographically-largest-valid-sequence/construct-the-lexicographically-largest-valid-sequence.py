class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        res = [0] * size
        used = [False] * (n + 1)

        def backtrack(index):
            if index == size:
                return True
            if res[index] != 0:
                return backtrack(index + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    res[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    res[index] = 0
                    used[1] = False
                else:
                    j = index + num
                    if j < size and res[index] == 0 and res[j] == 0:
                        res[index], res[j] = num, num
                        used[num] = True
                        if backtrack(index + 1):
                            return True
                        res[index], res[j] = 0, 0
                        used[num] = False
            return False

        backtrack(0)
        return res
