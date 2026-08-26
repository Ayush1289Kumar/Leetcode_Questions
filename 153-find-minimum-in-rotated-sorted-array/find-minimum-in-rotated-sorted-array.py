class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n -1
        ans = 0

        while (start <= end):
            guess = (start+end)//2

            if nums[guess] > nums[n-1]:
                start = start+1
            else:
                ans = guess
                end = guess -1
        
        return nums[ans]