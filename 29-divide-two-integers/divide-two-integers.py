class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= temp + temp:
                temp += temp
                multiple += multiple
            dividend -= temp
            result += multiple

        return -result if negative else result
