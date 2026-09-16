class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        if temp<0:
            return False

        while(temp!=0):
            rem = temp%10
            temp//=10
            rev=rev*10+rem
        
        return x == rev

