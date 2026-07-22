class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) -1
        k=0

        while(left<=right):

            if nums[left] == val and nums[right]!= val:
                nums[left] ,nums[right] = nums[right],nums[left]
                k+=1
                left+=1
                right-=1
        
            elif nums[right] == val:
                right-=1
            else:
                k+=1
                left+=1
        return k 
