class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {'b':1,'a':1,'l':2,'o':2,'n':1}
        map = {}

        for c in text:
            map[c] = map.get(c,0)+1
        
        ans = float("inf")

        for c in balloon:
            if c not in map:
                return 0    
            times = map[c]//balloon[c]
            ans = min(times,ans)
        
        return ans