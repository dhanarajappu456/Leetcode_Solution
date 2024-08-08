class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        step =0 
        direct =[(0,1),(1,0),(0,-1),(-1,0)]
        dir_ =  0 
        ans.append((rStart,cStart))
        while(len(ans)!=rows*cols):


            #we need to increease the step by one when going in east or west

            if dir_ ==0  or dir_ ==2:
                step+=1 

            #move in current direction with the "step" number of steps

            for i in range(step):
                rStart,cStart = rStart+direct[dir_][0] , cStart+ direct[dir_][1]
                if (0<=rStart<=(rows-1) ) and (0<=cStart<=(cols-1)):
                    ans.append((rStart,cStart))
                
                
            #change the direction
            dir_ = (dir_+1)%4

        return(ans) 


