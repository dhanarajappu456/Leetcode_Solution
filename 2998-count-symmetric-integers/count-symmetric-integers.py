class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def symm(x):
            
            if len (str(x))%2 ==0:
                n = len(str(x))//2
                num  = str(x)
                num_arr =[int(c) for c in num]
                #print(num_arr)
           
                if sum(num_arr[0:n]) == sum(num_arr[n:]):
                    #print("jk")
                    return True
            return False
            
           
        ans = 0
        for num in range(low,high+1):
            if symm(num):
                ans+=1
        return ans 
        