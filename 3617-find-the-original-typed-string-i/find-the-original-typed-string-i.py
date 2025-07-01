class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        variations = set()
        variations.add(word)

        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            length = j - i
            if length > 1:
                for l in range(1, length):
                    new_word = word[:i] + word[i:i + l] + word[j:]
                    variations.add(new_word)
            i = j

        return len(variations)
