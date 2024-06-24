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



solution 3 o(1) space

- same idea as of solution 2 , but not using the set dsa 

instead modify those flipped position in the nums array itself , with some value to mark it

so that extra space not used 
t n 
s 1 

'''



#solution 3 - modifying nums array, so as to not use the extra space(set)
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        '''
        
        '''
        n =len(nums)
        #keeps count of how many times current element
        #need to be flipped
        flip_count =  0
        for i,num in enumerate(nums):
            #checks if the flipcount contain
            #flip from invalid window before( ie, window far more than k dist )
            #in which case it need to be discarded , so count is reduced, 
            #as that flip from any element in that window 
            # don't influence the current element
            if (i-k) >=0 and (nums[i-k]  == -1  ):
                flip_count-=1
            #flipping current element
            current   = (num + flip_count)%2 

            #if current element is still  0 , 
            #then we need to flip it 
            if current == 0:
                #in case when there is no sufficient
                #k element(icluding current element)
                #we can't perform flip , so return -1 
                if (i+ k) >n:
                    return -1 
                flip_count+=1
                nums[i]=-1

        return nums.count(-1)
            
            





        