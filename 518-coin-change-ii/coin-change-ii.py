class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    
        num = coins
        n = len(num)
        tar = amount
        #1 using take or not take

        
        
        # memo = [[-1 for i in range(tar+1)] for j in range(n)]
        
        # def rec(ind,tar):
        #     if tar ==0:
        #         return 1
        #     if ind ==0:
        #         return int(tar%num[0]==0)
        #     if memo[ind][tar]!=-1:
        #         return memo[ind][tar]
            
        #     take = 0
        #     if tar>= num[ind]:
        #         take   = rec(ind,tar-num[ind])
        #     notTake = rec(ind-1,tar)
        #     memo[ind][tar] = take + notTake
        #     return  memo[ind][tar]
        
        # return  rec(n-1,tar)



        
        2# trying out all combination  with remaining amount , but notice  , we have tp be careful not repeat same    #combination there fore it is essential to not consider the elment already considered


        




        @lru_cache(None)
        def rec(ind, rem):

            if rem ==0:
                return 1
            elif rem <0 :
                return 0

            
            cnt=0
            for ind in range(ind,n):

                if rem>= num[ind]:
                   cnt+=rec(ind, rem-num[ind])
            return cnt
        return rec(0, tar)


            
