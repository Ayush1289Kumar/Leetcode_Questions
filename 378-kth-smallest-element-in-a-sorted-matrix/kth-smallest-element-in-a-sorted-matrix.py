class Solution:
    def LessThan(self,matrix,m,n,guess):
        row = m-1
        col = 0
        cnt = 0
        while (row>=0  and col < n):
            if matrix[row][col] <= guess:
                cnt+= row+1
                col+=1
            else:
                row-=1
        
        return cnt

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        low = matrix[0][0]
        high = matrix[m - 1][n - 1]
        ans = -1

        while (low<=high):
            guess = (low+high)//2
            num = self.LessThan(matrix,m,n,guess)
            if num < k:
                low = guess+1
            else:
                ans = guess
                high = guess - 1
        
        return ans