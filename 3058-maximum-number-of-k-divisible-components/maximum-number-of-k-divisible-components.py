'''
it doesn't matter , if we formed a component on the subtree
that is the values are used or not , we can always return 
all the values from the subtree, but whwen sub component
has a multiple of k , that is when increment the answer
'''

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        adj  = defaultdict(list)

        for a,b in edges: 
            adj[a].append(b)
            adj[b].append(a)

        for a in range(0,n):
            if len(adj[a])<=1:
                root = a 
                break
        root = 0 
        self.cnt = 0
        vis = set()
        def rec(root):
            vis.add(root)
            ans  = values[root]
            for nb in adj[root]:
                if nb not in vis:
                    val = rec(nb)
                    ans+= val
            if ans%k==0:
                self.cnt +=1
            return ans
        rec(root)
        return self.cnt