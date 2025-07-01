class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        result = ""

        for i in range(len(s)):
            temp = self.expand(s, i, i)
            if len(temp) > len(result):
                result = temp
            temp = self.expand(s, i, i + 1)
            if len(temp) > len(result):
                result = temp

        return result

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
