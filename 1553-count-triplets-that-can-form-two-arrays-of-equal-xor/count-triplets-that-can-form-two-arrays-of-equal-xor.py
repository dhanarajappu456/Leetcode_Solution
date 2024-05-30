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



'''

class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        res= 0
        n =len(arr)
        xor = 0 
        mp_cnt  = defaultdict(int)
        mp_prev_ind_sum = defaultdict(int)
        mp_cnt[0]=1
        mp_prev_ind_sum[0] = 0
        for i in range(n):
            xor ^= arr[i]
            if xor in mp_cnt:
                res+= i*mp_cnt[xor] - mp_prev_ind_sum[xor]
            mp_cnt[xor]+=1
            mp_prev_ind_sum[xor]+= (i+1)
        return res
        