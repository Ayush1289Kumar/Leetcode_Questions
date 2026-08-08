class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0])
        
        initial_start = intervals[0][0] 
        initial_end = intervals[0][1]

        ans = []


        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if initial_end >= start :
                initial_end = max(initial_end,end)
                continue
            
            
            ans.append([initial_start,initial_end])
            initial_start = start
            initial_end = end

        ans.append([initial_start,initial_end])
        
        return ans