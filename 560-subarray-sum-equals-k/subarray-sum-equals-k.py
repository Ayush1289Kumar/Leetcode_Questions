class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        curr_sum = 0
        ans = 0

        for i in range(len(nums)):
            curr_sum+=nums[i]

            if curr_sum - k in freq: 
                ans+= freq[curr_sum - k]
            
            freq[curr_sum] = freq.get(curr_sum,0)+1
        
        return ans