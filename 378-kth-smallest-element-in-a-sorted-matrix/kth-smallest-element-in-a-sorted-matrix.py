class Solution:
    def isLessThan(self,matrix,m,n,guess,k):
        row = m - 1
        col = 0
        cnt = 0

        while (row>= 0 and col < n):
            if matrix[row][col] <= guess:
                cnt += row+1
                col+=1
            else:
                row-=1
        
        return cnt >= k
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        low = matrix[0][0]
        high = matrix[m-1][n-1]
        ans = -1

        while (low<= high):
            guess = (low+high)//2

            if self.isLessThan(matrix,m,n,guess,k):
                ans = guess
                high = guess - 1
            else:
                low = guess + 1
        
        return ans