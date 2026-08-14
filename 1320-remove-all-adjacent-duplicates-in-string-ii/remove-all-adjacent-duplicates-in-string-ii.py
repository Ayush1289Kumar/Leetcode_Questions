class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in range(len(s)):
            if len(stack)==0:
                stack.append([s[i],1])
                continue
            if stack[-1][0] == s[i]:
                stack[-1][1] +=1

                if stack[-1][1] == k:
                    stack.pop()
                continue
            
            stack.append([s[i],1])
        
        ans = ""
        
        for i in range(len(stack)):
            ans += stack[i][0] * stack[i][1]

        return ans