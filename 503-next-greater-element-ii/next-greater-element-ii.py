class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        stack =[]
        for i in range(n-2,-1,-1):
            stack.append(nums[i])
        
        for i in range(n-1,-1,-1):

            while len(stack)!=0 and stack[-1] <= nums[i]:
                stack.pop()
            
            if len(stack)==0:
                ans[i] = -1
            
            else:
                ans[i] = stack[-1]
            
            stack.append(nums[i])
        
        return ans