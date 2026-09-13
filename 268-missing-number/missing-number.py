class Solution:
    def swap(self,nums,n1,n2):
        temp = nums[n1]
        nums[n1] = nums[n2]
        nums[n2] = temp

    def cyclicSort(self,nums,n):
        i = 0
        while (i<n):
            if (nums[i] < n and nums[i] != i ):
                self.swap(nums,i,nums[i])
            else:
                i+=1
         
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        self.cyclicSort(nums,n)

        for i in range(n):
            if nums[i] != i:
                return i
        
        return n