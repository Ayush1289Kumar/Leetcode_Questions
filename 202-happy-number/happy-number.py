class Solution:

    def sum_of_squares(self,n):
        sum = 0

        while n:
            rem = n%10
            n = n//10
            sum+= rem*rem
        
        return sum
        
    def isHappy(self, n: int) -> bool:
        slow = fast  = n

        while (fast!=1):
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(fast)
            fast = self.sum_of_squares(fast)

            if slow == fast and slow!=1:
                return False
        return True
        