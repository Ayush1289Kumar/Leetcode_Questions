class Solution:
    def max(self, map):
        max_val = 0
        max_key = None

        for key, value in map.items():
            if value > max_val:
                max_val = value
                max_key = key

        return max_key

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        ans = []

        # Create frequency map
        for i in nums:
            map[i] = map.get(i, 0) + 1

        # Find maximum k times
        for i in range(k):
            key = self.max(map)
            ans.append(key)
            del map[key]

        return ans