class Solution:
    def swap(self,nums,n1,n2):
        temp = nums[n1]
        nums[n1] = nums[n2]
        nums[n2] = temp
    
    def cyclicSort(self,nums,n):
        i = 0
        while (i<n):
            correct = nums[i] -1
            if (nums[i] > 0 and nums[i] <= n and  nums[i] != nums[correct]):
                self.swap(nums,i,correct)
            else:
                i+=1
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        self.cyclicSort(nums,n)
        for i in range(n):
            if nums[i] != i+1:
                return i+1


        return n+1