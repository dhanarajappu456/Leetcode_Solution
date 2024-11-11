class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x 
        i_x = 1 
        i_n = 1 
        while(i_n <= (n-1)):
            #fill the bit in the places wehre 
            #there is 0 in the x
            if i_x & x == 0 :
                #fill the current bit in the value n-1 , pointer by i_n
                #to the slot indicated by i_x on the x  
                #also note that if it 0 pointed by i_n 
                #jsut ignore it , as  it is already 0 
                #in the x, just move to the next poistion in x , ie 
                #move the i_x to next bit posotion  
                if (n-1 ) & i_n !=0:
                    res |= i_x
                #moving the pointer i_n , on the bits of value 
                #represneted by n-1 
                i_n = i_n<<1
            #moving the pointer on bits of x ,
            #to dfind the next empty slot on x 
            i_x  = i_x<<1
        return res
