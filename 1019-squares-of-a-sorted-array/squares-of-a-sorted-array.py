class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []

        for i in nums:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)
        
        def square(arr):
            for i in range(len(arr)):
                arr[i] = arr[i]*arr[i]
        
        square(positive)
        square(negative)
        negative.reverse()

        n1 = n2 = 0
        m = len(negative)
        n = len(positive)

        ans = []

        while (n1 < m and n2 < n):
            if negative[n1] < positive[n2]:
                ans.append(negative[n1])
                n1 += 1
            else:
                ans.append(positive[n2])
                n2 += 1
        while (n1 < m):
            ans.append(negative[n1])
            n1 += 1

        while (n2 < n):
            ans.append(positive[n2])
            n2 += 1
        return ans