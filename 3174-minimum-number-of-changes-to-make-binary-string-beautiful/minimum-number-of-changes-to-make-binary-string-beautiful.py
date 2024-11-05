class Solution:
    #the idea is that , a valdi partiton can be broken to 
    #furhter small even partion at the end giving a parition with 
    #two elements

    #so it is matter of checking for block of two elements like 
    #what are the changes that we need 
    def minChanges(self, s: str) -> int:
        i =1
        n= len(s)
        count = 0
        ans  = 0 
        while(i<n):
            #if current block two elemetn has , contrasting 
            #elements then we need to change either one of it
             
            if s[i]!=s[i-1]:
                ans+=1
            i+=2
        return ans


        