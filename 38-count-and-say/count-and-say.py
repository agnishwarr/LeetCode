class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"

        for _ in range (n-1):
            next=[]

            i=0
            while i<len(s):
                j=i
                while j<len(s) and s[j] == s[i]:

                    j+=1
                next.append(str(j-i))
                next.append(s[i])
                i=j
            s="".join(next)
        return s