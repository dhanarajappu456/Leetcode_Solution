class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list )
        n = len(edges)+1
        for a,b in edges:

            adj[a].append(b)
            adj[b].append(a)

            if len(adj[a]) == n-1:
                return a
            if len(adj[b]) == n-1:
                return b
