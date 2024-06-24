'''
solution 1 - bruteforce  - simulation - changing the array as we traverse 

so this might include flipping all element in current window and then next window starts from next 
0th element. 


t nk
s  1 


solution 2 - what if we already know number of time
currrent element that need to be flipped.
here we keep a vaiable that keep track of flipCount , which is 
the varible denoting the number of flips the current element need to do 

but remember , a flip in a window doesnt contribute to flipping an element outside and next to it
 it so we need to decrement this by 1 

t n 
s n


'''

#solution 2 
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        '''
        
        '''
        n =len(nums)
        flip_count =  0
        flipped  = set()
        for i,num in enumerate(nums):
            if (i-k) >=0 and ((i-k )in flipped ):
                flip_count-=1
            current   = (num + flip_count)%2 
            if current == 0:
                if (i+ k) >n:
                    return -1 
                flip_count+=1
                flipped.add(i)
        return len(flipped)
            
            





        