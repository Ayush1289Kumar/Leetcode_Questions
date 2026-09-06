class Solution:
    def hours(self,nums,size,speed):
        hr = 0

        for i in range(size):
            hr += nums[i]//speed

            if nums[i]%speed != 0:
                hr+=1
        
        return hr
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 0
        size = len(piles)
        low = 1
        high = max(piles)

        while(low <= high):
            speed = (low+high)//2
            hour = self.hours(piles,size,speed)

            if (hour>h):
                low = speed+1
            else:
                ans = speed
                high = speed -1
        
        return ans