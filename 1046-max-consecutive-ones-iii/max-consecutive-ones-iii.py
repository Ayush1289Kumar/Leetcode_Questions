class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = max_num = 0
        n = len(nums)

        freq = {0:0,1:0}

        for high in range(n):
            freq[nums[high]]+=1

            while freq[0] > k:
                freq[nums[low]] -= 1
                low+=1
            
            max_num = max(max_num,high-low+1)
        
        return max_num