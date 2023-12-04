class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans  = -1
        res = ""
        n = len(num)
        i=0
        while(i<n):

            if 1<=i<=n-2 and num[i-1] == num[i] and num[i] == num[i+1]:

                 if ans<int(num[i-1:i+2]) :
                    ans = int(num[i-1:i+2])
                    res = num[i-1:i+2]
         
            i+=1
            
        
        return res
    

            
        