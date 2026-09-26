import heapq as h
import math
class Pairs:
    def __init__(self,dist,idx):
        self.dist = dist
        self.idx = idx
    
    def __lt__(self,other):
        # Max-Max heap

        if self.dist != other.dist:
            return self.dist > other.dist
        return self.idx > other.idx

class Solution:
    def distance(self,x,y):
        return math.sqrt(x**2+y**2)

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        n = len(points)

        heap =[]
        ans = []
        for i in range(k):
            dist = self.distance(points[i][0],points[i][1])
            h.heappush(heap,Pairs(dist,i))

        for i in range(k,n):
            dist = self.distance(points[i][0],points[i][1])
            if heap[0].dist > dist:
                h.heappop(heap)
                h.heappush(heap,Pairs(dist,i))
        

        for i in heap:
            idx = i.idx
            ans+= [points[idx]]
        
        return ans

        