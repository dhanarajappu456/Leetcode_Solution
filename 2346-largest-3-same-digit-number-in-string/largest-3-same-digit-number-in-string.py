class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans  = -1
        res = ""
        n = len(num)
        i=0
        while(i<n-2):

            good = True
           
            for j in range(2):
                if num[i+j]!=num[i+j+1]:
                    good = False
                    break
            
        
            if good:
              
                if ans<int(num[i:i+3]) :
                    ans = int(num[i:i+3])
                    res = num[i:i+3]
                i+=3
            else:
                i+=1
            
        
        return res
    

            
        