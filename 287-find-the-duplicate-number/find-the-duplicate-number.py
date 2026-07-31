class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while (True):
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if fast == slow:
                slow = 0
                while (slow !=fast):
                    fast = nums[fast]
                    slow = nums[slow]
                
                return slow
