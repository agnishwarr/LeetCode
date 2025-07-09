class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []
        num = 1
        
        for ch in pattern:
            stack.append(str(num))
            num += 1
            if ch == 'I':
                while stack:
                    res.append(stack.pop())
        
    
        stack.append(str(num))
        while stack:
            res.append(stack.pop())
        
        return ''.join(res)
