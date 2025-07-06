class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        res = []
        for i in range(word_len):
            left = i
            right = i
            window_count = {}
            count = 0
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                if word in word_count:
                    window_count[word] = window_count.get(word, 0) + 1
                    count += 1
                    while window_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    if count == len(words):
                        res.append(left)
                else:
                    window_count.clear()
                    count = 0
                    left = right
        return res
