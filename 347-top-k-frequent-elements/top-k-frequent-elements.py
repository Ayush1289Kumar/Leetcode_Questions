import heapq as h

class Pairs:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def __lt__(self,other):
        if self.first != other.first:
            return self.first > other.first
        return self.second > other.second

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        map = {}
        ans = []

        for i in nums:
            map[i] = map.get(i,0)+1    # element -> frequency
        
        for key,value in map.items():
            h.heappush(heap,Pairs(value,key))
        
        for i in range(k):
            ans.append(h.heappop(heap).second)

        return ans