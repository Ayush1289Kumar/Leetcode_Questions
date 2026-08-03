class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]

        for move in moves:
            if move=="U":
                pos[0]+=1
            
            elif move=="D":
                pos[0]-=1
            
            elif move=="R":
                pos[1]+=1
            
            else:
                pos[1]-=1
        
        return pos[0]==0 and pos[1]==0
        
