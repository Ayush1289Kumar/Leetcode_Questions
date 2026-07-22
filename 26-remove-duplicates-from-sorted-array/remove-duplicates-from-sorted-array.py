class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        k=1
        
        for i in range(1,len(nums)):
            if nums[i-1] !=nums[i]:
                nums[first+1] = nums[i]
                first+=1
                k+=1
        
        return k

        