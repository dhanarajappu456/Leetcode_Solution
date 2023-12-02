class Solution:
    def sumZero(self, n: int) -> List[int]:
        '''
        one strategy is to append  number from 1 as 
        1, -1 , 2 , -2 , 3, -3 and so on 

        if n was odd, then we will at end add 0 to the list

        t n 
        s 1 (excluding the result array space)

        '''
      
        ans = [ ]
        val = 1
        while(n>1):
            
            ans.append(val)
            ans.append(-val)
            val+=1
            n-=2
        if n:
            ans.append(0)
        return ans





        