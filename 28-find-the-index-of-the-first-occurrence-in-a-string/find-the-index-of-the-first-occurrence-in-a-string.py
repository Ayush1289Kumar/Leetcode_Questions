class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_str = ""
        n,k = len(haystack),len(needle)
        low = 0
        high = k

        if k==0: return 0

        if k > n: return -1 

        for i in range(k):
            window_str+=haystack[i]
        
        if window_str == needle:
            return 0

        while (high < n):
            window_str = window_str[1:]
            window_str += haystack[high]

            high+=1
            low+=1

            if window_str == needle:
                return low
            
        
        return -1
        

