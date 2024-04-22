class Solution:
    def smallestNumber(self, pattern: str) -> str:

        ans  = ""

        def rec(ind,s,used,prev):
            nonlocal ans 
            
            if ind==len(pattern):
                ans  = s 
                return True
           
            if pattern[ind]=="I":
             
                for i in range(prev+1,10):
                    
                    if (i not in used ):
                        used.add(i) 
                        if rec(ind+1, s+str(i),used,i):
                            return True
                        used.remove(i)
            else:
                for i in range(prev-1,0,-1):
                    if (i not in used ):
                        used.add(i) 
                        if rec(ind+1, s+str(i),used,i):
                            return True
                        used.remove(i)
            return False
        used = set()
        
        for i in range(1,10):
            used.add(i)
            if rec(0,str(i),used,i):
                return ans
            used.remove(i)
        return ""


        