'''

solution -1 
bruteforce for i,j,k

t n^3
s 1

solution 2 - optimisation to n^2
the questioncan be interpreted in another way 
that is it asks to find subarry whose len>=2 and
xor of all elements in it  =0 
so we find possible subaray with i at left and k at right
when we find such subarry with xor =0 with left end at i and right end at k , then 
we could have k-i possiblities for j , which is added to result 

t n^2
s 1


solution 3 - optimisation to n- using prefix xor and maps

we can optimise the solution 2 using a preifx map, like technique used to find 
subarray with target sum.
here we keep on finding the prefix xor , and when at a particular index k , 
our aim is to find the , subarray with sum 0 (ie, whose left is at i and right at k)

suppose there is a subarray from i to k then there are k-i options for j and thus (k-i) 
added to result 

mp_cnt
-----------------------------
the mp_cnt keeps track of count of prev xors found so far , so we can remove this prefix xor 
from current xor ending at k , to get the xor =0 

but the portions with value say "xor"  that can be removed might be at many position(giving several left end i for 
current  k ) 
and for each such possiblities there might be some number of options for each j . 

say suppose 1,1,1,2,3,1 
for current index (k) ending at 5, we have a subarray with xor value = 0 with  i at 3 and 1, 

and for subarray with i at 3  we have 2 options for j 
and for subarray with i at 0  we have 2 options for j 4
so total ans for k=5 is 6 , 

If we know the number of times we have seen 1 (xor to be removed) so far be p.
and 1 as prev_xor found at 0(we store 0+1 in mp_prev_ind_sum) and 2(we store 2+1 in mp_prev_ind_sum) let this 
sum be q

so the ans  = k*p - q 
and this p is stored in mp_cnt and q is stored in mp_prev_ind_sum.
mp_prev_ind_sum is nothing but it stores sum of all  index+1 where the value xor occurs

t n
s 1
'''

class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        res= 0
        n =len(arr)
        xor = 0 
        #keeps count of each xor seen so far 
        mp_cnt  = defaultdict(int)
        #keeps sum of all indices + 1
        mp_prev_ind_sum = defaultdict(int)
        mp_cnt[0]=1
        mp_prev_ind_sum[0] = 0
        for i in range(n):
            xor ^= arr[i]
            #if there is a portion with xor value to be removed 
            #so that we can get subarray with xor alue - 0 , ranging from i to k 
            #we have foudn the required subarrays .
            #This is assuming subarray initially ranging from 0 to k 
            #then subtracting each of index where it occurs
            #essentially giving number of options of j for each of them
            if xor in mp_cnt:
                res+= i*mp_cnt[xor] - mp_prev_ind_sum[xor]
            mp_cnt[xor]+=1
            mp_prev_ind_sum[xor]+= (i+1)
        return res
        