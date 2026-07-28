class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        basket ={}
        ans = -1
        
        for high in range(len(fruits)):
            basket[fruits[high]] = basket.get(fruits[high],0)+1
            
            while (len(basket) > 2):
                basket[fruits[low]]-=1
                
                if basket[fruits[low]] == 0:
                    del basket[fruits[low]]
                low+=1
            
            if len(basket) <= 2:
                window_length = high-low+1
                if ans<window_length:
                    ans = window_length
            
        return ans