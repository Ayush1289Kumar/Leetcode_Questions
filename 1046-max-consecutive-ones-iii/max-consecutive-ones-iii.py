class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = max_num = 0
        zero_count = 0

        for high in range(len(nums)):
            if nums[high] == 0:
                zero_count+=1
            
            while (zero_count > k):
                if nums[low] == 0:
                    zero_count-=1
                low+=1
            
            max_num = max(max_num,high-low+1)
        
        return max_num