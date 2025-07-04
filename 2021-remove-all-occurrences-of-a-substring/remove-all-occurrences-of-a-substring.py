class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        plen = len(part)

        for ch in s:
            stack.append(ch)
            if len(stack) >= plen and ''.join(stack[-plen:]) == part:
                del stack[-plen:]

        return ''.join(stack)
