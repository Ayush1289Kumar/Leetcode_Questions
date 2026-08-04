class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_delete = arr[0]
        one_delete = float("-inf")
        ans = arr[0]

        for i in range(1,len(arr)):
            prev_nodelete = no_delete

            no_delete = max(no_delete+arr[i],arr[i])

            one_delete = max(one_delete+arr[i],prev_nodelete)

            ans = max(ans,one_delete,no_delete)
        
        return ans


            
