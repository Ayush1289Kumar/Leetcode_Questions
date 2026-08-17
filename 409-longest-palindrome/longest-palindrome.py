class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0)+1
        
        ans = 0
        hasOdd = False

        for value in freq.values():
            if value%2 == 0:
                ans+=value
            else:
                ans+=value-1
                hasOdd = True
        
        if hasOdd:
            return ans+1

        return ans