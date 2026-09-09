class Solution:
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in matrix:
            arr.extend(i)

        arr.sort()
        return arr[k-1]
