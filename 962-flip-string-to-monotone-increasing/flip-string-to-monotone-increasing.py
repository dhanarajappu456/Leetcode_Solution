class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:


        '''

        decision to flip current character depends up on the last character of the monotonic string made uptil current index-1 , 
        
        so we need to have this character passed on the sucessive call as the prev character 
        
       

    also since the state (ind, prev)  - > is overlpaping subproblem we can cache it 
        '''


        n = len(s)

        @lru_cache
        def rec(ind , prev):




            if ind ==n :
                return 0 
            ans  = float("inf")


            curr =s[ind]
            if prev == "0":

                if curr =="0":
                    
                    ans = min(ans , rec(ind+1, "0" ) , 1+ rec(ind+1, "1"))
                    

                elif curr=="1":


                     ans = min(ans , 1 +  rec(ind+1, "0" ) , rec(ind+1, "1"))

                return ans
            elif prev =="1":
                if curr =="0":
                    ans = min(ans ,1+ rec(ind+1, "1"))
                elif curr=="1":
                     ans = min(ans ,   rec(ind+1, "1"))
                return ans
        return rec(0 , "0")





   

        