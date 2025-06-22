class Solution:
    def maxDistance(self, st: str, k: int) -> int:
    
        n,w,s,e  = 0,0,0,0
        steps = 0 
        ans  = 0 
        final_man  = 0
        current_man  =0
        for i,c in enumerate(st):
            if c  == "N":
                n+=1
            if c  == "S":
                s+=1
            if c == "W":
                w+=1
            if c == "E":
                e+=1
            
            current_man  = abs(w-e) + abs(s-n)
            steps = i+1
            extra_possible = 0 
            if current_man != steps:
                wasted  = steps - current_man
                extra_possible  =  min(2*k, wasted)
            final_man  =  current_man + extra_possible

            ans  = max(ans, final_man)
        return ans
            
            
            
            