import heapq as h

class Pairs:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def __lt__(self,other):
        if self.first != other.first:
            return self.first < other.first
        return self.second < other.second

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        map = {}
        ans = []

        for i in nums:
            map[i] = map.get(i,0)+1    # element -> frequency
        
        for key,value in map.items():
            if len(heap) < k:
                h.heappush(heap,Pairs(value,key))
            elif heap[0].first < value:
                h.heappop(heap)
                h.heappush(heap,Pairs(value,key))
        
        while heap:
            ans.append(h.heappop(heap).second)
        
        return ans