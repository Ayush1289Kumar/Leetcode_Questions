class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1=p2=0
        m = len(word1)
        n = len(word2)

        str=""

        while (p1 < m and p2 < n):
            
            str+=word1[p1]
            str+=word2[p2]
            p1+=1
            p2+=1
        
        while (p1<m):
            str+=word1[p1]
            p1+=1
        
        while (p2<n):
            str+=word2[p2]
            p2+=1

        return str