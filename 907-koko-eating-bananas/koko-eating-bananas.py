class Solution:

    def possibleHours(self,nums,size,speed):
        hour = 0

        for i in range(size):
            hour += nums[i]//speed

            if nums[i]%speed !=0:
                hour+=1
        
        return hour
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        size = len(piles)
        start , end = 1, max(piles)
        ans = 0

        while (start <= end):
            guess_speed = (start+end)//2

            hourNeeded = self.possibleHours(piles,size,guess_speed)

            if hourNeeded > h:
                start = guess_speed+1
            else:
                ans = guess_speed
                end = guess_speed-1
        
        return ans