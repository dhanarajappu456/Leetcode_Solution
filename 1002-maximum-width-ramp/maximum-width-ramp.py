'''
solution 1 brute force

t n^2
s 1 

solution2 - optimised solution - using monottonic decreasing stk and bin search

the idea is if current element is greater than previous element this current element can't be 
the left side of any ramp , since left side of a ramo need to be as far as to wards left. 
this paves a stack or ds of decresing order to be formed ,  which therefore acn be used to do a binary search 
to find the element with left most element in the stk with height<= current element
t nlogn 
s  n(stk)

solution3- optimised solution - greedy 

we sort the array based in value also we will have their old index saved
thus as we iterate on this sorted array ,which is the right leg
of the ramp , we need to get the min index among all the values 
to the left of this value in array , 

therefore we also keep track of the min index in the values 
seen so far , so that we can find the max ramp dist 
that current element can from with it beign right leg


t nlogn 
s  n(stk)
'''


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mono_stk =[]
        n = len(nums)
        ans = 0 
        arr =[]

        for i,num in enumerate(nums):
            arr.append((num,i))
        arr.sort()
        left_ind  = arr[0][1]
       
        for num, ind in arr[1:]:
            ans = max ( ans , ind - left_ind ) 
            if left_ind > ind :
                left_ind  = ind
        return ans 



        