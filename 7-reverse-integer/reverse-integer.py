class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        isNegative = False
        if(x<0):
            isNegative = True
            x = -x

        while(x>0):
            rem = x%10
            x//=10
            rev=rev*10 + rem
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
            
        if isNegative:
            return -rev
        return rev
        