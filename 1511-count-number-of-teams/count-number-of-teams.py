class Solution:
    def numTeams(self, rating: List[int]) -> int:


        arr1 =[ 0 for i in range(max(rating)+ 2)]
        arr2 =[ 0 for i in range(max(rating)+ 2)]
        ans  = 0 
        n  = len(rating)
        for i in range(n-1):
            n1 = rating[i]
       
            for j in range(i+1,n):
                n1,n2= rating[i],rating[j]

                if n1<n2:
                    ans += arr1[n1-1]
  
                if n1>n2:
                    ans+= arr2[n1+1]
            for i in range(n1,len(arr1)):
                arr1[i]+=1
            for i in range(1,n1+1):
                arr2[i]+=1
            

        return ans
        