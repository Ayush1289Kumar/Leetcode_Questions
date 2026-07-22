class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        second = 1
        k = 1
        
        while (second < len(nums)):
            if nums[second] != nums[second-1]:
                nums[first+1] = nums[second]
                first+=1
                k+=1
            second+=1

        return k