class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        #start choosing the subsequence from the 0th index
        #then from the 1st index
        #choose the best sequence u can get  among each of them
        n  =len(nums)
        last_rem = -1
        count = 0 
        odd,even  =0 ,0 
        alt = 0 

        #finding the odd nums
        for i in range(n): 
            if nums[i]%2!=0:
                odd+=1
        #finding the even nums 
        for i in range(n ):
            if nums[i]%2  ==0:
                even+=1
        #finding the alternating parity numbers
        for i in range(n):
            if nums[i]%2 != last_rem:
                last_rem   = nums[i]%2 
                count+=1
        alt  = max(alt, count)

        return   max(odd, even, alt)