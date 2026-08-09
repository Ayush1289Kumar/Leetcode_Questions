class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        p1 = p2 = 0
        ans = []

        while (p1 < m and p2 < n):
            low = firstList[p1][0]
            high = firstList[p1][1]
            start = secondList[p2][0]
            end = secondList[p2][1]

            # Check if overlapping, if overlapping is there there must be intersection 
            if max(low,start) <= min(high,end):
                ans.append([max(low,start),min(high,end)])
                

            if high <= end:
                p1+=1
            
            else:
                p2+=1
        
        return ans