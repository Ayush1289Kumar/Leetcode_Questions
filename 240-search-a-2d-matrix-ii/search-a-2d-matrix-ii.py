class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        val = []
        for i in matrix:
            val.extend(i)

        return target in val

