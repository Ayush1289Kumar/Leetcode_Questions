class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]

        result = abs(nums[0])

        for i in range(1,len(nums)):
            v1 = max_sum + nums[i]
            v2 = min_sum + nums[i]
            v3 = nums[i]

            max_sum = max(v1,v2,v3)
            min_sum = min(v1,v2,v3)

            result = max(result,abs(max_sum),abs(min_sum))
        
        return result
            