class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # if not intervals and not newInterval:
        #     return []

        inserted = False

        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i,newInterval)
                inserted = True
                break

        if not inserted:
            intervals.append(newInterval)

        ans = []

        low = intervals[0][0]
        high = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if high>=start:

                high = max(high,end)
                continue

            ans.append([low,high])
            low =start
            high = end
        
        ans.append([low,high])

        return ans