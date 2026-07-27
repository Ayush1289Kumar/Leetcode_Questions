class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min = float("inf")
        low = high = sum = 0

        while (high<len(nums)):
            sum += nums[high]

            while(sum>=target):
                curr_min = high-low+1
                if curr_min < min:
                    min = curr_min 
                sum-= nums[low]
                low+=1
            high+=1
        
        return min if min!=float("inf") else 0

