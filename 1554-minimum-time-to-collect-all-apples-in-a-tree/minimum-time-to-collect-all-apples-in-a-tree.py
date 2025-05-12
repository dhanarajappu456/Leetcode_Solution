from collections import defaultdict as dict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:



        adj = dict(list)
        for e in edges:

            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        # par to mark as parent, which is already visited
        def rec(root,par):
            time  =0 
            ans = 0 
            for nb in adj[root]:
                if par!= nb:
                    time += rec(nb,root)
                
            ans  += time
            if hasApple[root] or time: 
                ans+=1
            #print(root, ans)
            return ans
        return max( 0 ,  (rec(0,-1) -1 )*2 )


