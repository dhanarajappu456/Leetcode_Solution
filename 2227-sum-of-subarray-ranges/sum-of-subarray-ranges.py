#solution 1 
#naive solution
#using 2 loop 

# class Solution:
#     def subArrayRanges(self, nums: List[int]) -> int:

#         n = len(nums)
#         ans = 0 
#         for i in range(n):
#             min_,max_ = nums[i],nums[i]
#             for j in range(i,-1,-1):
#                 min_,max_ = min(min_,nums[j]),max(max_,nums[j])
#                 ans += (max_ - min_)
#         return ans


# t n^2 
# s n 



# solution 2 
#mono stack , 

'''
if u closely see this , rather than summing the diff for each subarryay 

if u carefully see the formula is

 sum ( all the possible max elements in some subbary) - sum(all possible min elements is some array)

 so we need to find for each element, if we know the subarray for which current element is the 
 max element , and do this for each element 

 similary the case to find the min element 

 these two things can be done with monotonic stack 
 a) for finding sum values where current element is the max 
  finding prev great and next great for each element 

  b) for finding sum values where current element is the min 
  finding prev small and next small for each element 
'''

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        nums = nums
        n = len(nums)
        ans = 0 
        prev_grt =[]
        prev_small =[]
        max_sum =0 

        #finding sum of all numbers that contribute to maximums in some array

        #prev_great -algo
        for right_ind,num in enumerate(nums+[float("inf")]):
            while(prev_grt and prev_grt[-1][0]<num):
                mid_val , mid_ind = prev_grt.pop(-1)
                left_val , left_ind  = prev_grt[-1] if prev_grt else (0,-1)
                max_sum +=(mid_ind-left_ind)*mid_val +(mid_ind-left_ind)*(right_ind-mid_ind-1) * mid_val
            prev_grt.append((num ,right_ind ))
        #finding sum of all numbers that contribute to minimum in some array
        #prev small - algo
        min_sum = 0
        
        for right_ind,num in enumerate(nums+[-float("inf")]):
            while(prev_small and prev_small[-1][0]>num):
                mid_val , mid_ind = prev_small.pop(-1)
                left_val , left_ind  = prev_small[-1] if prev_small else (0,-1)
                min_sum +=(mid_ind-left_ind)*mid_val +(mid_ind-left_ind)*(right_ind-mid_ind-1) * mid_val
            prev_small.append((num ,right_ind ))
        #ans = sumof maximum  -sum of minimum
        return (max_sum - min_sum)

    

# t n^2 
# s n 




        