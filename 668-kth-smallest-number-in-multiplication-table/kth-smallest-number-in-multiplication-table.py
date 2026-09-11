class Solution:
    def LessThan(self,m,n,guess):
        cnt = 0
        for i in range(1,m+1):
            cnt+= min(guess//i,n)    

        return cnt

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low = 1
        high = m*n
        ans = -1

        while (low<=high):
            guess = (low+high)//2
            num = self.LessThan(m,n,guess)
            if num < k:
                low = guess+1
            else:
                ans = guess
                high = guess - 1
        
        return ans