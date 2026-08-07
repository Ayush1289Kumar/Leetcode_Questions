class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr_sum = 0
        freq = {0:-1}
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr_sum+=(-1)
            
            else:
                curr_sum += 1
       
            
            if curr_sum in freq:
                ans = max(ans, i-freq[curr_sum])
            
            else:
                freq[curr_sum] = i
        return ans


