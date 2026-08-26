class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_value = max(arr)
        return arr.index(max_value)
