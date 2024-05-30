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
        for i in range(n-1):
            xor = arr[i]
            for k in range(i+1,n):
                xor^=arr[k]
                if xor ==0 :
                  
                    res+=  (k-i)
        return res
        