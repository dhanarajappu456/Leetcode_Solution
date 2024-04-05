class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:



        #create the graph(adj list)
        #for each of the person , run dfs and find the  connected nodes and find the min of quietness
        #of all the values

        adj  = defaultdict(list)
        for a,b in richer:
            adj[b].append(a)
      
        vis = set()
        def dfs(node):
            vis.add(node)
            min_ans,min_ind = quiet[node],node
            for neib in adj[node]:
                if neib not in vis:
                    res,ind= dfs(neib)
                    if res<min_ans:
                        min_ans = res
                        min_ind = ind 
            return min_ans,min_ind
        
            
        res = []
        for n in range(len(quiet)):
            vis  = set()
            ans,ind  = dfs(n)
            res.append(ind)
        return res
        

        