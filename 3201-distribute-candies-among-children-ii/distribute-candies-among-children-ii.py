
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        #THE best solution is to find the ans in o(N)

        #here we will need to distribute the candies to the first 
        #child let it be a number of candies ,  
        #then for the second and the third , let their sum be b+c, 

        # which is n - a 

        '''
        the b+c should   
        x <=  b+c <= min(limit,n-a)

        where x is the number of candies that the second child can take
        so that the third child's candy wont exceed the limit for the 
        third child
        '''
        # 

        ans  = 0 
        for a in range(min(limit,n)+1):
            '''
            there can be case when the remaining candies , after giving the first child , that is
            n-a , is less than limit  in which case the we can't give the limit number of candies 
            to the third child
            '''
            x = max(0, n-a -  limit)

            ans  += max(0 ,  min(limit, n-a) - x +1)
        return ans

            



            



        return ans 
        