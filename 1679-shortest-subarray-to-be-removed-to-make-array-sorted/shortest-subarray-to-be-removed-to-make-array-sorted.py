class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = n
        i,j = 0 , n-1
        while(j>0 and   arr[j]>=arr[j-1]):
            j-=1

        #in case 15, 10,1,2,3,4,5,6 
        #front portion might need ro be removed which is == j 
        print(j)
        ans  = min(ans, j)


        while(i<j and (i==0 or arr[i]>= arr[i-1])) :
            while(j<n and arr[i]>arr[j]):
                j+=1
            ans  = min(ans , j-i-1)
            i+=1

        return ans 