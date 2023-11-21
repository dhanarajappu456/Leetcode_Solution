'''

solution is simple, 

let value at i be a and j be b 

since we know we need pair with 
a+ rev(b) = rev(a)+b
= a-rev(a) = b-rev(b)
which means we need the pairs such that the diff between the number and its reverse are same for both number 


so as we traverse we keep track of these difference and the count of numbers that have the same diff, 
from which we can find the number of such pair
'''

from collections import defaultdict as dict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def reverse(num):
            rev = 0

            while(num):

                rev = (rev*10)+num%10 
                num//=10

            return rev
        MOD  = 10**9+7
        # maps  the difference(num - rev(num) ) -> count of numbers with same difference
        diff_count = dict(int)
        
        res =0 
        for i,num in enumerate(nums):
            
            diff_count[num -reverse(num)]+=1
            #calculate the number os such pair with this diff
            res   = (res%MOD +   (diff_count[num -reverse(num)]-1)%MOD)%MOD

        return res 


        