'''
#solution 1 -  greedy

the idea is any pair of number in the tree can be maximised if possible to maximise both , without
affecting other numbers in the path b/w these number.

initially we find ideal(max sum) that can be obtained from all the numbers in the tres

note: if number of numbers in the tree that can be maximised is odd ,  then one of the number  which is maximised 
using xor with k , is need to be undone, since , there is no other number forming pair with this  .
 thus we subtract(undo xoring a number num with k) min_xor_diff from the ideal sum
  
  note:
  min_xor_diff = the minimum diff b/w a number  and its xored value , among all of the xored values
'''


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        #no of number which yield higher value on xoring with k 
        count= 0
        #minimum xored value
        min_xor_diff = float("inf")

        #stores ideal(max) sum that is obtained after performing xor with k (for each num )
        ans = 0 
        #finding ideal sum and count  number that can be maximised by  xoring with k
        for num in nums:
            #if xoring yields higher number , then xor it to get max(ideal) sum
            if num^k> num:
                count+=1 

                ans += (num^k)
            #if it doesn't yield a higher num, then consider the num as such
            else:
                ans += num
            #stores the min diff b.w its value and xored value withk 
            min_xor_diff = min(min_xor_diff,abs(num - ( num^k)))
        #if no;of numbers that can yield hiher nums on xor with k , is odd
        #then undo one such operation , by removing the mindiff from the ideal sum
        if count%2==1:
            return ans  - min_xor_diff
        #if even then ideal sum  == final result
        return ans