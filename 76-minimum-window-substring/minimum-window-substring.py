class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        freq = [0] * 128

        for ch in t: 
            freq[ord(ch)] +=1

        low = high = start = 0
        required = len(t)
        min_len = float("inf")
        
        while high < len(s):
            h = s[high]

            if freq[ord(h)] > 0:
                required -= 1
            
            freq[ord(h)] -=1
            high+=1

            while required == 0:
                if high-low < min_len:
                    min_len = high - low
                    start = low
                
                l = s[low]
                freq[ord(l)] += 1 

                if freq[ord(l)] > 0:
                    required += 1
                
                low += 1
        
        return "" if min_len == float("inf") else s[start:start + min_len]