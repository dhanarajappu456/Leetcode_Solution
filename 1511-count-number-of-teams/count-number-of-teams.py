class Solution:
    def numTeams(self, rating: List[int]) -> int:

      
        ans =0 
        n  = len(rating)
        @lru_cache(None)
        def rec(prev_ind,inc,cnt):
            if cnt ==3:
               
                return 1 
            res =0
            for i in range(prev_ind+1,n):
                
                if inc==True  and (prev_ind == -1 or rating[i]>rating[prev_ind]):
                    res+= rec(i,True,cnt+1)
                elif inc ==False  and (prev_ind == -1 or rating[i]<rating[prev_ind]):
                    res+=rec(i,False,cnt+1)

            return res

        return rec(-1,True,0) + rec(-1,False,0)


