class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

            # S = P+P
            # S+S = P+P+P+P
            # Trimming = [1:-1] => P+P 
            
            duplicate = s+s
            trimmed = duplicate[1:-1]

            return s in trimmed
