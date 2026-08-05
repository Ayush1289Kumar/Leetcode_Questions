class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        curr_sum = 0
        ans = 0

        for i in range(len(nums)):
            curr_sum+=nums[i]

            rem = curr_sum % k

            if rem<0:
                rem+=k
            
            if rem in freq:
                ans+=freq[rem]
            
            freq[rem] = freq.get(rem,0)+1
        
        return ans