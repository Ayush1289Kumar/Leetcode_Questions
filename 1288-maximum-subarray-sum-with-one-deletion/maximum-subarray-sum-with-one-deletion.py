class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        delete = float('-inf')
        noDelete = arr[0]
        ans = arr[0]

        for i in range(1, n):

            v1 = arr[i]
            v2 = noDelete + arr[i]
            v3 = delete + arr[i]
            v4 = noDelete

            noDelete = max(v1, v2)
            delete = max(v3, v4)

            ans = max(ans,delete, noDelete)
        
        return ans