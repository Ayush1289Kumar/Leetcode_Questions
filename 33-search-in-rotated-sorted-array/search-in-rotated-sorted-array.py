class Solution:

    def minV_idx(self,nums):
        min_idx = 0
        start , end = 0, len(nums) -1

        while(start<=end):
            mid = (start+end)//2

            if (nums[mid] < nums[min_idx]):
                min_idx = mid
                end = mid-1
            else:
                start = mid+1
        
        return min_idx
    
    def binarySearch(self,s,e,nums,target):
        start, end = s, e

        while (start <= end):
            mid = (start+end)//2

            if nums[mid] < target:
                start = mid+1
            
            elif nums[mid] > target:
                end = mid-1
            
            else:
                return mid
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # First we will find the minimum index and then we will break the array in two parts, and we will apply binary search in that parts.
        s1, e1 = 0, self.minV_idx(nums)
        s2, e2 = self.minV_idx(nums), len(nums)-1

        ans = -1
        ans = self.binarySearch(s1,e1,nums,target)

        if ans==-1:
            ans = self.binarySearch(s2,e2,nums,target)

        return ans
        
        