class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        if k == 1:
            return 'a'

        n = len(operations)
        length = 1
        for i in range(n):
            length *= 2
            if length >= k:
                op_type = operations[i]
                new_k = k - length // 2
                break

        res = self.kthCharacter(new_k, operations[:i])
        if op_type == 0:
            return res
        if res == 'z':
            return 'a'
        return chr(ord(res) + 1)
