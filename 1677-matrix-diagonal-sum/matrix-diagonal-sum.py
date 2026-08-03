class Solution:
    def diagonalSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        total = 0
        for i in range(n):
            total += matrix[i][i]             
            total += matrix[i][n - 1 - i]     

        if n % 2 == 1:
                total -= matrix[n // 2][n // 2]    
        
        return total
