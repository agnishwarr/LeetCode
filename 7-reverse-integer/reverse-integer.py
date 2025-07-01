class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit = 2**31
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            result = result * 10 + digit

        result *= sign

        if -limit <= result < limit:
            return result
        return 0
