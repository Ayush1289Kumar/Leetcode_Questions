class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        low = 0
        max_fruits = 0
        basket ={}

        for high in range(n):
            basket[fruits[high]] = basket.get(fruits[high],0)+1

            while (len(basket) > 2):
                basket[fruits[low]]-=1

                if basket[fruits[low]] == 0:
                    del basket[fruits[low]]
                
                low+=1
            
            curr_fruits = high-low+1
            max_fruits = max(curr_fruits,max_fruits)
        
        return max_fruits 
