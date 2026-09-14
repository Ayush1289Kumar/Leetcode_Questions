class Solution:   
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while (i<n):
            correct = nums[i]
            if (nums[i] < n and nums[i] != nums[correct]):
                nums[correct],nums[i] = nums[i],nums[correct]
            else:
                i+=1
        
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n