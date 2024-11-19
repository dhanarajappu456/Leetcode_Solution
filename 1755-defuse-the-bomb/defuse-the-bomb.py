class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N
        win_sum = 0 
        if k!=0:
        
            win_sum = sum(code[1:k+1]) if k>0 else sum (code[k:])
   
        for i in range(N):
            res[i] = win_sum
            if k<0:

                win_sum -= code[(N+k+i)%N]
                win_sum+= code[i%N]
                 
            elif k>0:
                
                win_sum -= code[(i+1)%N]
                win_sum+= code[(i+k+1)%N]


           
        return res