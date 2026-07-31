class Solution:

    def max_value(self,arr):
        max_ = 0
        for i in arr:
            if i > max_:
                max_ = i
        return max_

    def characterReplacement(self, s: str, k: int) -> int:
        low = length_substring = 0
        freq = [0] *256
        n= len(s)

        for high in range(n):
            freq[ord(s[high])] += 1

            window_len = high-low+1
            max_int = self.max_value(freq)
            
            diff = window_len - max_int
            while (diff > k):
                freq[ord(s[low])] -= 1
                low+=1
                max_int = self.max_value(freq)
                window_len = high-low+1
                diff = window_len - max_int
            
            if length_substring < window_len:
                length_substring = window_len
    
        return length_substring


            