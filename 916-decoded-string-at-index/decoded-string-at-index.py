class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        '''
        the idea to find the position kth character in each of the multiplied sub-parts
        for this we calculate the length of entire string , then , we check the position of the required character
        in each multiplied sub-parts, startng from the entire string length , from backward


        '''
        tot_len  = 0

        #calculating the entire string length
        for i,c in enumerate(s):
        
            if c.isdigit():

                tot_len*= int(c)
            else:
                tot_len += 1
        
        #iterating from the end , we find the position k relative to each suparts
        for i in range(len(s)-1, -1 ,-1):

            

            c = s[i]
            k%=tot_len 
            #if the current character is the  character needed then return it 
            #note we need to check the current char is not a digit as well
            #else it fails in some cases like 
            # "a23" , k  =6 
            if c.isalpha() and k ==0 :
                print(tot_len)
                return c
            
            if c.isdigit():
                tot_len//=(int(c))
            else:
                tot_len-=1
        

