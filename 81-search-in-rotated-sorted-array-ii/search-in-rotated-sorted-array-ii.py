class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        start, end = 0, n - 1

        while start <= end:
            mid = (start + end) // 2

            # Duplicate case
            if nums[start] == nums[mid] == nums[end]:
                if nums[mid] == target:
                    return True

                start += 1
                end -= 1
                continue

            # Part 1 -> Left half is sorted
            if nums[start] <= nums[mid]:

                if nums[mid] == target:
                    return True

                elif nums[start] <= target < nums[mid]:
                    end = mid - 1

                else:
                    start = mid + 1

            # Part 2 -> Right half is sorted
            else:

                if nums[mid] == target:
                    return True

                elif nums[mid] < target <= nums[end]:
                    start = mid + 1

                else:
                    end = mid - 1

        return False