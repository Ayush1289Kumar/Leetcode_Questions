class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lower = 0
        upper = m*n -1

        while (lower <= upper):
            middle = (lower+upper)//2
            row = middle//n
            col = middle%n
            if matrix[row][col] < target:
                lower = middle + 1
            elif matrix[row][col] > target:
                upper = middle - 1
            else:
                return True
        
        return False

        