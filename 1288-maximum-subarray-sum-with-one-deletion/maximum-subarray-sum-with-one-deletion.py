class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_delete = arr[0]
        one_delete = float("-inf")
        ans = arr[0]

        for i in range(1,len(arr)):
            prev_onedelete = one_delete
            prev_nodelete = no_delete

            no_delete = max(no_delete+arr[i],arr[i])

            if (prev_nodelete == float("-inf")):
                value = arr[i]
            else: 
                value = prev_onedelete + arr[i]
            
            one_delete = max(value,prev_nodelete)

            ans = max(ans,max(one_delete,no_delete))
        
        return ans


            
