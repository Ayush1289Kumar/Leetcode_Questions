class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sor = sorted(nums)
        rev = sorted(nums,reverse=True)


        return nums==sor or nums==rev