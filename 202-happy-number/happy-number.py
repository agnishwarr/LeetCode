class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            
            new_n = 0
            while n > 0:
                digit = n % 10
                new_n += digit * digit
                n //= 10
            n = new_n
        
        return True
