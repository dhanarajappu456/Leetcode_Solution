# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


'''

we can do the linear search ,but that would exceed 100 calls to the get() method

so we use binsearch


1) find the peak 
if the peak is the target, immediately return it as it would be the first ocuurence of the target 
2)do seperate bin search on ascend and descend parts 

find the index of the target in the first part ,if it is not in first part then find it in second half, 

remember ther will not be duplicate  number in a particular half, as the array is mountain
'''
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        n =mountain_arr.length()
        l=0
        r = n-1
        ind =-1
        peakInd  = -1
        while(l<=r):
            m= (l+r)//2
        
            if ( m+1<n-1 and mountain_arr.get(m)<mountain_arr.get(m+1)):
                
                l= m+1 
            else:
                peakInd  = m
             
                r= m-1
        #if peak is the targt elment ,immediately return peak ind
        if mountain_arr.get(peakInd) == target:
            return peakInd 
  
        #find index of target in left half , if it is present 
        s,e = 0,peakInd
        while(s<=e):
            mi =(s+e)//2
            if mountain_arr.get(mi)   ==target:
               
                return mi
            elif target<mountain_arr.get(mi):  
                e = mi-1
            else:
                s =mi+1 
            
        #find index of target in right  half , if it is present 
        s,e = peakInd,n-1
        while(s<=e):
            mi =(s+e)//2
            if mountain_arr.get(mi) ==target:
                ind = mi
                return mi
            elif target<mountain_arr.get(mi):
                s = mi+1
            else:
                e =mi-1 
            
        return(ind)


        
        