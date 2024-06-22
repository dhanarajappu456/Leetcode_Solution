'''
solution 2
sliding window 
the sliding window cannot be applied as such 

eg: 
conside 2,2,1,1,1,2,2  and k = 3 
in this example the when at ind = 5,6 the we can still form the subarray with 3 elements 
with i at 0,1,2. So it is important that  when we shrink the i , of the window , 
we need to store this information of how many elements at beginning is removed,
so that the window still has k elements .
Since these removed elements can form subarray with even elements coming afterwards 
as discussed above. 
t n
s 1

'''


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
 
        i,j = 0,0
        n = len (nums)
        #keeps number of odd numbers in current window /subarray
        odds = 0
        ans =0 
        #this keeps the number of elements that can be removed from 
        #beginning of current subarray so that still number of odds 
        #in this subarray that end at j 

        prevCount =  0
        while(j<n):
            #when current number if odd, we update the odds , prevCount
            if nums[j]%2 ==1:
                prevCount =  0
                odds+=1
            #find prevCount 
            #ie,find the number of elements that can be removed from front so that 
            #the subarray still have k number of odds in it
            while(odds == k):
                if nums[i]%2 ==1:
                    odds-=1
                prevCount+=1
                i+=1
            #add the prevCount(which is the  number of suabrray with k elemetns in it and end 
            #at j )
            ans+= prevCount
            j+=1
        return ans 
                
            
            
            
            
            
            