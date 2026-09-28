class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while(left<=right):
            guess = (left+right)//2

            if nums[guess] < target:
                left = guess+1
            
            elif nums[guess] > target:
                right = guess-1
            else:
                return guess
        
        return -1