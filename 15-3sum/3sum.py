class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if (i>0 and nums[i] == nums[i-1]):
                continue
            
            left = i+1
            right = len(nums)-1

            while(left<right):
                sum = nums[left] + nums[right]
                if (sum == -1*nums[i]):
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    
                    while (left<0 and nums[left] == nums[left-1]):
                        left+=1
                
                    while (right>0 and nums[right] == nums[right+1]):
                        right-=1
                
                elif (sum < -1*nums[i]):
                    left+=1
                else:
                    right-=1
            
        return res
