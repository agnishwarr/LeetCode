class Solution(object):
    def longestCommonPrefix(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""

        prefix = words[0]

        for word in words[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
