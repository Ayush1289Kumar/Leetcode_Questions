class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <=2:
            return len(nums)
        start = 1
        current = 2

        
        while (current < len(nums)):
            if nums[current] != nums[start -1]:
                start+=1   
                nums[start] = nums[current]
            
            current+=1
        
        return start+1