class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = p2 = 0
        ans=[]
        m = len(nums1)
        n = len(nums2)
        median = 0
        while p1<m and p2<n:
            if nums1[p1] < nums2[p2]:
                ans.append(nums1[p1])
                p1+=1
            
            elif nums2[p2] < nums1[p1]:
                ans.append(nums2[p2])
                p2+=1
            
            else:
                ans.append(nums1[p1])
                ans.append(nums2[p2])
                p1+=1
                p2+=1
                
        while (p1<m):
            ans.append(nums1[p1])
            p1+=1
        
        while p2<n:
            ans.append(nums2[p2])
            p2+=1
        
        total_length = len(ans)

        if total_length%2==0:
            pos1=total_length//2 - 1  # n/2 -1
            pos2=total_length//2 # n/2 
            median = (ans[pos1] + ans[pos2])/2
        
        else:
            pos = total_length//2
            median = ans[pos]
        
        return median

            