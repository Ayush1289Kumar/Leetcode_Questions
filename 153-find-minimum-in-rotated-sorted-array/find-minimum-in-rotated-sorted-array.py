class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = nums[0]

        start , end  = 0,len(nums)-1

        while (start <= end):
            mid = (start+end)//2

            if nums[mid] < min_value:
                min_value = nums[mid]
                end = mid -1
            else:
                start = mid +1
        
        return min_value