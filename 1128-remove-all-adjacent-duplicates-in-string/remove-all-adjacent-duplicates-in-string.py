class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if len(stack)==0 or stack[-1]!= s[i]:
                stack.append(s[i])
            
            else:
                stack.pop()
        
        return "".join(stack)