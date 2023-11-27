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
#solution 2
class Solution:


    def knightDialer(self, n: int) -> int:
        mod = 10**9+7

        map_   = {
             0:[4,6], 
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7: [2,6],
            8:[1,3],
            9:[2, 4]}
        memo ={ }
        #current value of cell at and n is rem number of jumps
        def rec(val,n):

            if n==0:
                return 1
            

            if (val,n) in memo:
                return memo[(val , n)]
            
            ans = 0 
            for v in map_[val]:

                ans = ( ans%mod +  rec(v,n-1)%mod)%mod
            memo[(val,n)] = ans
            return ans


        ans  = 0 
        for val in range(0,10):
            
            ans  = (ans%mod +  rec(val,n-1)%mod)%mod 
        return ans 

        return ans
            





                    
            

            

        