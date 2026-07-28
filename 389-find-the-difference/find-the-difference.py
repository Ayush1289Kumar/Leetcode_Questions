class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        
        if s == t[0:-1]:
            return t[-1]

        for i in range(len(t)-1):
            if s[i] != t[i]:
                return t[i]

            
        
        
