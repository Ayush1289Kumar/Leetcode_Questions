class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        ans=""

        for i in range(len(s)):
        
            if len(stack)==0:
                stack.append([s[i],1])
            
            elif stack[-1][0] != s[i]:
                stack.append([s[i],1])
            
            else:
                if stack[-1][1] < k-1:
                    stack[-1][1] += 1
                else:
                    stack.pop()
        
        for i in range(len(stack)):
            ans+= stack[i][0] * stack[i][1]
        
        return ans