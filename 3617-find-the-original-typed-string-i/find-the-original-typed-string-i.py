class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans  =  0
        # arr  = [ 0 for i in range(26)]
        # for c in (word):
        #     arr[ord(c)- 97]  +=1
        # print( arr )
        # for i in range(26):
        #     ans+= max(0, arr[i] -1)
        # return ans + 1
        n = len(word)
        i,j  = 0 , 0 
        while(i< n):
            j = i 
            count = 0
            while(j<n and  (word[j] == word[i])):
                j+=1
                count+=1
            #every character except last contiguous set of characater ,
            #contribute count -1 times 

            #and last contiguous character contribute coount times
            ans+= max(0, count-1)   
            i = j
        return ans + 1 

            
            
        