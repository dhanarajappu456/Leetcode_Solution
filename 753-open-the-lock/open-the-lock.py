from collections import deque as deq 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int: 
        q = deq([ ])
        deadends = set(deadends)
        if "0000" not in deadends:
            q.append(("0000",0))
       
        vis   =  set()
        vis.add("0000")
        
        while(q):
            #print(q)
            val, step  = q.popleft()    
            
            if val  == target:
                return step
            val  = list(val)
            for i in range(4):
                
                newVal1 = val.copy()
                newVal1[i] = str((int(newVal1[i]) + 1 )%10)
                newVal1 = "".join(newVal1)
                if newVal1 not in vis and newVal1 not in deadends:
  

                    vis.add(newVal1)
                    q.append( ( newVal1 , step+1))

                #back move is important 
                #eg say target is 0009 then 
                #ans must be 1 , if we followed forward moves, the ans would have been 9 
                newVal2 = val.copy()
                newVal2[i] = str((int(newVal2[i]) - 1 )%10)
                newVal2 = "".join(newVal2)
            
                if newVal2 not in vis and newVal2 not in deadends:
  

                    vis.add(newVal2)
                    q.append( ( newVal2 , step+1))
        return -1 