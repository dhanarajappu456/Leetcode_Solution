class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        
        tot_len  = 0
        for i,c in enumerate(s):
        
            if c.isdigit():

                tot_len*= int(c)
            else:
                tot_len += 1
        
        
        for i in range(len(s)-1, -1 ,-1):

            #if the current character is the  character needed then return it 

            c = s[i]
    
            k%=tot_len 

            if c.isalpha() and k ==0 :
                print(tot_len)
                return c
            
            if c.isdigit():
                tot_len//=(int(c))
            else:
                tot_len-=1
            #print(k,tot_len)
            

