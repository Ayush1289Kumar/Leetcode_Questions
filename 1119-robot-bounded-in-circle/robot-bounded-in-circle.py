class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x , y = 0,0

        left,right = 0,1

        for i in instructions:
            if i=='G':
                x+=left
                y+=right

            elif i=='L':
                left,right = -right,left
                
            else:
                left,right = right,-left
                
        
        return (x==0 and y==0) or (left,right)!=(0,1)
            

