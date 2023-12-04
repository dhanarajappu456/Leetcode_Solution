

'''
Example - 1

the solution is simple , that , we try the bruteforce backtracking way of 

partitioning the  word 


t:


one way to code this is take or not take pattern wher we need 


curr ind, prev val and prev part index, as the paramter passed

where we make a partition at current index,  or not make partition at current index, 

so time = 2^n  = 2^20 = 10^6

s = n 

'''


class Solution:
    def splitString(self, s: str) -> bool:
        
        n  = len(s)
        def rec(ind, prev_val , parts):

            if ind  == n : 
                return parts>=2

            for i in range(ind,n):
                curr = int(s[ind:i+1]) 
                #if it is the first partition , then we have no prev val to 
                # compare, with  so directly make partition , 

                # else we need to make partition at i , such that s[ind: i+1] is 1 less then prev value
                if parts ==0 or  curr == prev_val-1:
                    if rec(i+1, curr, parts+1):
                        return True
            return False
        return rec(0,-1, 0)







                