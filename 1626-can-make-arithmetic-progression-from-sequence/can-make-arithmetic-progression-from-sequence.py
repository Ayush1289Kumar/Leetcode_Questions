class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        curr_diff = abs(arr[0] - arr[1])
        diff=float("inf")

        for i in range(2,len(arr)):
            new_diff = abs(arr[i] - arr[i-1])
            
            diff = new_diff-curr_diff

            if diff!=0:
                return False
        
        return diff==0 if len(arr)>2 else True


        
