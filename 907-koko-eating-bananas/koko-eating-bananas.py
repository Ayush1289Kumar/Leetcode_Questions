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
        start = 1
        end = max(piles)

        while(start <= end):
            speed = (start+end)//2
            hour = self.hours(piles,size,speed)

            if (hour>h):
                start = speed+1
            else:
                ans = speed
                end = speed -1
        
        return ans