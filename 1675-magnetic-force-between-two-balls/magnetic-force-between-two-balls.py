class Solution:
    def canPlace(self,position,n,m,guess):
        ball = 1
        pos = position[0]

        for i in range(n):
            distance = position[i] - pos
            if distance < guess:
                continue
            ball+=1
            pos = position[i]
        
        return ball >= m
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        low = 1
        high = position[n-1] - position[0]
        ans = -1
        while (low <= high):
            guess = (low+high)//2

            if self.canPlace(position,n,m,guess) :
                ans = guess
                low = guess + 1
            else:
                high = guess - 1
    
        return ans