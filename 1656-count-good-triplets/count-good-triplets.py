class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt  = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    x,y,z  = arr[i],arr[j],arr[k]
                    #print(x,y,z, abs(x-y) , "-", a  ,  abs(y-z) ,"-",b   , abs(x  -z),"-",c, ( abs(x-y) <= a ) and ( abs(y-z)<= b) and ( abs(x  -z)<=c)  )
                    if ( ( abs(x-y) <= a ) and ( abs(y-z)<= b) and ( abs(x  -z)<=c) ) :
                        cnt+=1
        return cnt