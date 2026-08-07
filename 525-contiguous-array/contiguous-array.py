class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero = one = 0
        freq = {0:-1}
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero+=1 
            else:
                one+=1

            diff = zero - one

            if diff == 0:
                ans = max(ans,i+1)
                continue
            
            if diff in freq:
                idx = freq[diff]
                length = i - idx
                ans = max(ans,length)
            
            else:
                freq[diff] = i
        
        return ans 