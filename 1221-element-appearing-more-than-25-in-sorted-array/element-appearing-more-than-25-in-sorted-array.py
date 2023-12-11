'''
solution3  - using builtin binsearch 
Binary search solution 
The idea  is that candidate element whose freq >25% would have its element in either of the parition for sure, 
thus we need to see all nums at index, n//4 , (2*n)//4 , (3*n)//4

t logn
s 1

'''

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        n = len(arr)
       
        candidates = {n//4 , 2*n//4 , 3*n//4}
        for i in candidates:
            print(i)
            if i < n :
                
                curr_num = arr[ i]  
               
                l = bisect.bisect_left(arr,arr[i])
                r = bisect.bisect_right(arr,arr[i])
             
                if r-l > (n//4):
                    return curr_num

            
            