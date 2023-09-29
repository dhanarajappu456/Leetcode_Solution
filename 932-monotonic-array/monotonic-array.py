
'''


using 2 flags inc , dec

at the end of the array , either inc or dec must be set , not both


'''


class Solution:
    def isMonotonic(self,nums):
        inc=1
        dec=1
        a=nums
        i=0
        while(i<len(nums)-1):
            if(a[i]>a[i+1]):
                inc=0
            if(a[i]<a[i+1]):
                dec=0
            i+=1       
        return(inc or dec)        
                