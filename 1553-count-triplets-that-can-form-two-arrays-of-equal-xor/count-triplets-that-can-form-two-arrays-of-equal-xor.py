class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        res= 0
        n =len(arr)
        for i in range(n-1):
            xor = arr[i]
            for j in range(i+1,n):
                xor^=arr[j]
                if xor ==0 :
                  
                    res+=  (j-i)
        return res
        