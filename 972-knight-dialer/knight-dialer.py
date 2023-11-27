'''


solution 1 - 3state

constructing the board and performing the recusrive solution with each cell as the starting cell

 note that a movement (ie, consisting of the 3 jump and in the shape of L as said in q) cannot end at non numeric cell  but out of the three jump intermediate cell can be  non numeric



 we can cahe the resut with state - i,j,n , when n is remaining number of jumps

t 3*4 *5000 *(8*3)  for each call we have inner loop runs for 8 direction (movements) and each direct has a jump of length 3 

so tot time approx = 10^5
 
s n(5000) 


solution 2- better optimised  and clean solution - without board- 2 state

instead if board we keep a map for each value mapped to possible values it can move , then we make use of this map 


t state reduce to to - (val,n) n =remaining number of jump  
time = 10 * 5000= 10^4 
s (n) = 5000



'''
#solution 1
class Solution:


    def knightDialer(self, n: int) -> int:
        board =[[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]

        mod = 10**9+7    
        memo  ={}
        def invalidCell(i,j):
            return board[i][j]==-1

        def out_bound(i,j):

            return i<0 or j<0 or i>=a or j>=b 
        def rec(i,j,n):

            
            
            #we can't stand at any non numerical cell out of each of the n-1 movementd
            if invalidCell(i,j):
                return 0

            # if we reach this line this will be a valid cell (ie, it is numerical cell )
            if n==0 :
                  
                return 1
      


            #for all possbilities check

            if (i,j,n ) in memo:
                return memo[(i,j,n)]
            ans = 0 
            
            for d in dire:
         
                x,y =i,j
                valid_cell =True
                for m in d:

                    x += m[0] 
                    y += m[1]
                    
                    if (not out_bound(x,y)):
                      
                        continue
                    else:
                      
                        valid_cell =False
                        break
                if valid_cell:
                   
                    ans  = (ans%mod + rec(x,y,n-1)%mod)%mod
            memo[(i,j,n) ] = ans%mod
            return ans

            


                    

    


        #for each number as the starting number:
        dire  = [
            
            [(-1,0),(-1,0),(0,-1)],[(-1,0),(-1,0),(0,1)],
        [(0,1),(0,1),(-1,0)],[(0,1),(0,1),(1,0)],
        [(1,0),(1,0),(0,-1)],[(1,0),(1,0),(0,1)],
        [(0,-1),(0,-1),(-1,0)],[(0,-1),(0,-1),(1,0)]]
        a,b = 4,3
        ans= 0 
        for i in range(a):
            for j in range(b):

                if board[i][j] !=-1:
                   
                    ans  = (ans%mod + rec(i,j,n-1)%mod)%mod
                 

        return ans


           
            
            

            

        