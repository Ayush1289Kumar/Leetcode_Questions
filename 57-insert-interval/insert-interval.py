class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        
        intervals.sort(key=lambda x:x[0])

        initial_start = intervals[0][0]
        initial_end = intervals[0][1]
        ans = []

        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
    
            if initial_end >= start:
                initial_end = max(end,initial_end)
                continue
            
            ans.append([initial_start,initial_end])
            initial_start = start
            initial_end = end

        ans.append([initial_start,initial_end])

        return ans