class Solution:
    def hours(self,nums,size,speed,h):
        hr = 0

        for i in range(size):
            hr += nums[i]//speed

            if nums[i]%speed != 0:
                hr+=1
        
        return hr <= h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 0
        size = len(piles)
        low = 1
        high = max(piles)

        while(low <= high):
            speed = (low+high)//2
            if self.hours(piles, size, speed, h):
                ans = speed
                high = speed - 1
            else:
                low = speed + 1
        
        return ans