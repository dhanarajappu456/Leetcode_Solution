'''
   
   solution 1 
        brute force - for each number calculate the diff, by iterating on the n eleements
        t n^2
        s 1(excludng the final ans array)
        n = len(nums)
    solution 2 -optimised - pref sum technique
    make use of sorted order  -

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


    t n 
    s n (pref sum)


    #solution 3 

    space o(1) solution 

    if u closely observe for each element we need  pref sum for all the element
    and sum till the element 

    so we can do this without pref array

    1)we calculate sum of all element as first step 
    2)for sum till current element- as we run the for lopp parallely compute the sum till current element



    t n
    s 1

    
'''

#solution 3 - space optimised
class Solution:
    
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        totPrefSum  = sum(nums)
        currPrefSum = 0 
        ans =[]
        for i in range(n):
           
            num = nums[i]
            currPrefSum+=num
            left = (i+1)*num - currPrefSum
            right = (totPrefSum-currPrefSum) - num*(n-1-i) 
            ans.append(left+right) 
        return ans
        