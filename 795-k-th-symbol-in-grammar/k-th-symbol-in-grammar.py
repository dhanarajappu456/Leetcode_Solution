class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        '''

        consider it as a graph and , since the position is n,k is given , we need to find teh postion of the 
        valus in the new grpah  as we traverse in a bst fashion . 
        like bst traversal 
        '''
        ans  = 0 
        i,j =0,0
        curr = 0
        while(n>0):

            if k<=2**(n-1):

                i,j = i+1, 2*j
                curr = 0  if curr ==0 else 1
                #move left


            else:
                i,j = i+1, 2*j+1
                k = k-2**(n-1)
                curr = 1 if curr ==0 else 0  
            ans = curr





            n-=1
           
        return ans

        