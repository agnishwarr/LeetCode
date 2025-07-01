class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        first = 1
        second = 2

        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second
