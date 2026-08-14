class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        stack = []
        ans = [0]*n

        for i in range(n-1,-1,-1):

            while len(stack) !=0 and temp[stack[-1]]<=temp[i]:
                stack.pop()
            
            if len(stack)==0:
                ans[i] = 0
            else:
                ans[i] = stack[-1] - i
            
            stack.append(i)
        
        return ans 
