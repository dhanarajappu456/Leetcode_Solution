from collections import deque as deq

#greedy dfs(dp)
class Solution:
    def minDays(self, n: int) -> int:
        
        memo  ={0 : 0 ,1: 1 }

        def rec(rem):
            

     
            
            if rem in memo:
                return memo[rem]
     
            choice1,choice2 =0,0
        
            if rem%2==0:
                choice1  = 1+rec(rem//2)
            else:
                choice1  = rem%2 + rec(rem-rem%2)
            
            if rem%3==0:
                choice2  = 1+rec(rem//3)
            else:
                choice2  = rem%3 + rec(rem-rem%3)
            memo[rem] = min (choice1,choice2)
            return memo[rem]

        return rec(n)


    # time :  at each time the rem divided by 2 and 3, so max number of subproblme is log(n, 2)
    # each takes o(1), so time = log(n,2)

    # space : o(log(n,2))
        

