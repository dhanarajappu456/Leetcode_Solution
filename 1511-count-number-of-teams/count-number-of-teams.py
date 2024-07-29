class Solution:
    def numTeams(self, rating: List[int]) -> int:

        #stores at any index i the total numbers less<=i and total numbers>=i

        arr1 =[ 0 for i in range(max(rating)+ 2)]
        arr2 =[ 0 for i in range(max(rating)+ 2)]
        ans  = 0 
        n  = len(rating)
        for i in range(n-1):
            n1 = rating[i]
       
            for j in range(i+1,n):
                n2,n3= rating[i],rating[j]
                #in this case , see how many number we have which<n2, 
                #which can act as n1, this can be found from arr1
                if n2<n3:
                    ans += arr1[n2-1]
                #in this case , see how many number we have which>n2, 
                #which can act as n1, this can be found from arr1
                if n2>n3:
                    ans+= arr2[n2+1]
            #updating the arr1 and arr2 info
            for i in range(n1,len(arr1)):
                arr1[i]+=1
            for i in range(1,n1+1):
                arr2[i]+=1
            

        return ans
        