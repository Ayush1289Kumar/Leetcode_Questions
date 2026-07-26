class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = two = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero+=1
            
            elif nums[i] == 1:
                one+=1
            
            elif nums[i] == 2:
                two+=1
        
        for i in range(len(nums)):
            if i in range(zero):
                nums[i] = 0
                continue
            
            if i in range(zero+one):
                nums[i] = 1
                continue
            
            else:
                nums[i] = 2

        