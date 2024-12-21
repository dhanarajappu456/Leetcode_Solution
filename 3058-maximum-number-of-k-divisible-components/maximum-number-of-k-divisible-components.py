class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        adj  = defaultdict(list)

        for a,b in edges: 
            adj[a].append(b)
            adj[b].append(a)

        root = 0 
        self.cnt = 0
        vis = set()
        def rec(root):
            vis.add(root)
            ans  = values[root]
            for nb in adj[root]:
                if nb not in vis:
                    val = rec(nb)
                    #a non neg
                    if (val!=-1):
                        ans+=val
            #if the 
            #1.root 
            #2 root and left 
            #3.root and right 
            # 4. root and left and right
            #is a multiple of k , then we assume to have 
            #used  those value and  return -1 , to indicated
            #no value returned byt his function, which wiil be checked
            #in upper calls that is in parent rec function 
            if (ans%k)==0:
                self.cnt +=1
                ans = -1
            return ans
        rec(root)
        return self.cnt