class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        max_diff = float("inf")
        sum = 0

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while (left < right):
                mySum = nums[left]+nums[right]+nums[i]
                
                diff = abs(target - mySum)

                if diff < max_diff:
                    max_diff = diff
                    sum = mySum
                    
                if (mySum == target):
                    return mySum
                
                elif (mySum < target):
                    left+=1
                
                else : 
                    right-=1
        
        return sum