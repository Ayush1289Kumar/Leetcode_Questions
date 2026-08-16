class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for c in s:
            if c in freq:
                freq[c] = freq.get(c)+1

            else:
                freq[c] = 1
        
        for k,v in freq.items():
            if v==1:
                return s.find(k)
        
        return -1

        