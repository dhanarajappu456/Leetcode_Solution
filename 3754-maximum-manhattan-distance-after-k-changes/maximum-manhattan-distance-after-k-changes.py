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
            #current net manhattan dist
            current_man  = abs(w-e) + abs(s-n)
            #max possible mandiat at a time
            steps = i+1
            #extrea movement that can be achieved using the k moves
            #note that on using each of the k moves, it increment the
            #mandist by +2 
            extra_possible = 0 
            if current_man != steps:
                wasted  = steps - current_man
                extra_possible  =  min(2*k, wasted)
            #this is the max man dist we can achieve at a poiny on using the k moves 
            final_man  =  current_man + extra_possible

            ans  = max(ans, final_man)
        return ans
            
            
            
            