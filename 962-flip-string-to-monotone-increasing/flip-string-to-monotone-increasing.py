class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        #when prev char is 0 i can have curr char as 0 or 1 , w
        #when prev char is 1 , i can only have curr char as1 


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





   

        