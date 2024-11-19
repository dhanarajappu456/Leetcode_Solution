class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        win_sum = 0 
        i,j  =0 ,0
        if k ==0:
            return [0 for i in range(n)]
        if k!=0:
            if k<0:
                i, j = n-abs(k) , n-1
                
            elif k>0 :
                i, j = 1 , k
            win_sum = sum (code[i:j+1])
               

            
   
        for k in range(n):
            res[k] = win_sum
            win_sum -= code[(i)%n]
            win_sum += code[(j+1)%n]
            print(code[(i+1)%n],  code[(j+1)%n])
            i = (i+1)%n
            j = (j+1)%n
            


           
        return res