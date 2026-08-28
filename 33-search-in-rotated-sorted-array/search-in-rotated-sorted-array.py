class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0,n-1

        while(start <= end):
            mid = (start+end)//2

            # Part 1 
            if (nums[mid] > nums[n-1]):
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] < target:
                    start = mid+1
                
                else:
                    if nums[0] <= target:
                        end = mid-1
                    else:
                        start = mid+1
            
            # Part 2
            else:
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    end = mid-1
                
                else:
                    if nums[n-1] >= target:
                        start = mid+1
                    else:
                        end = mid-1
            
        return -1
