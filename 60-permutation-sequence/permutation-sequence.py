import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1
        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result.append(numbers.pop(index))
            k %= fact

        return ''.join(result)
