class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        for i in range(k):
            window_sum+=nums[i]
        
        max_sum = window_sum
        low=0
        high=k

        while (high<len(nums)):
            window_sum = window_sum - nums[low] + nums[high]

            if window_sum > max_sum:
                max_sum = window_sum
            
            low+=1
            high+=1
        return max_sum/k