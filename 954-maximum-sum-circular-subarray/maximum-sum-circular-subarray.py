class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        total_sum = nums[0]
        ans = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]


        for i in range(1, len(nums)):
            total_sum += nums[i]

            v1 = curr_max + nums[i]
            v3 = nums[i]
            curr_max = max(v1,v3)
            max_sum = max(max_sum,curr_max)

            v2 = curr_min + nums[i]
            curr_min = min(v2,v3)
            min_sum = min(min_sum,curr_min)

            ans = max(max_sum,ans)
        
        if max_sum < 0:
            return max_sum
        
        return max(ans,total_sum-min_sum)

