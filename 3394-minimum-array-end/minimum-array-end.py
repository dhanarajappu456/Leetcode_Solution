class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x 
        i_x = 1 
        i_n = 1 
        while(i_n <= (n-1)):
            #fill the bit in the places wehre 
            #there is 0 in the x
            if i_x & x == 0 :
                if (n-1 ) & i_n !=0:
                    res |= i_x
                i_n = i_n<<1
            i_x  = i_x<<1
        return res
