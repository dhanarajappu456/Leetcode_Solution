'''
   
   solution 1 
        brute force - for each number calculate the diff, by iterating on the n eleements
        t n^2
        s 1(excludng the final ans array)
        n = len(nums)
    solution 2 -optimised
    make use of sorted order

    for each number which are less than nums[i]
    
    abs diff with elements left of  it is 
    where nums[i] is current element 
    this nums[i] - nums[j] where j is index of elements to left of it  
    this can be formalised to the equation prefsum till 
    
    left =  num[i]- (i+1)*nums[i]

    similarly for right part of i, which are all greater than nums[i]

    equation is  
    
    right = (pref[n-1]-pref[i]) - num*(n-i-i) 

    thus total ans  = left + right
    
'''
class Solution:
    
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pref =[0 for i in range(n)]
        pref[0] = nums[0]
    
        for i in range(n):
            num = nums[i]
            pref[i] = pref[i-1]+nums[i]
        

        ans =[]
        for i in range(n):
            num = nums[i]
            left = (i+1)*num - pref[i]
            right = (pref[n-1]-pref[i]) - num*(n-1-i) 

            ans.append(left+right) 
        return ans
        