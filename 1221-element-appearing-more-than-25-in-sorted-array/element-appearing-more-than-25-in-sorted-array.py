'''
solution3 
Binary search solution 
The idea  is that candidate element whose freq >25% would have its element in either of the parition for sure, 
thus we need to see all nums at index, n//4 , 2n//4 , 3n//
[0 - n//4], [n//4+1 ,2n//4] , [2n//4+1 , n]
'''

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        n = len(arr)
        def bin_left_most(i):
            curr_num = arr[i]
            l= 0
            h=  i

            ans  =i

            while(l<=h):
                m =(l+h)//2
                if arr[m] ==  arr[i]:
                    ans = m
                    h= m-1
                else:
                    l = m+1
            return ans
        def bin_right_most(i):

            curr_num = arr[i]
            l= i
            h=  n-1
            ans = i
            while(l<=h):
                m =(l+h)//2
                if arr[m] ==  arr[i]:
                    ans = m
                    l = m+1
                else:
                    h = m-1
            return ans
        
        for i in {n//4 , 2*n//4 , 3*n//4}:
            
            if i < n :

                curr_num = arr[ i]  
               
                l = bin_left_most(i)
                r = bin_right_most(i)
              
                if r-l+1 > (n//4):
                    return curr_num

            
            