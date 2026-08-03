class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0

        # Player A = +1  and Player B = -1
        for i,(r,c) in enumerate(moves):
            val =1 if i%2==0 else -1

            rows[r]+=val
            cols[c]+=val

            if r==c:
                diag+=val
            if r+c == 2:
                anti_diag+=val
            
            # Check if player gets 2 in a line

            if 3 in (rows[r],cols[c],diag,anti_diag):
                return "A"
            
            if -3 in (rows[r],cols[c],diag,anti_diag):
                return "B"
        
        return "Draw" if len(moves) == 9 else "Pending"