import heapq as h

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        heap = []

        for i in range(k):
            h.heappush(heap,nums[i])
        
        for i in range(k,n):
            if nums[i] > heap[0]:
                h.heappop(heap)
                h.heappush(heap,nums[i])

        return h.heappop(heap)