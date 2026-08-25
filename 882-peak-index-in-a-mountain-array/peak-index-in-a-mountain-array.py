class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr)-1
        ans = 0

        while (start<end):
            mid = (start+end)//2

            if arr[mid] < arr[mid+1]:
                start = mid +1
            
            else:
                end = end-1
                ans = end
        
        return ans