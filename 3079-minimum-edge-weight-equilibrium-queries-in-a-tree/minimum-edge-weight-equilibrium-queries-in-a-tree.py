from collections import defaultdict as dict


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        # create adjlist - for dfs traverssal
        adj = dict(list)
        for n1, n2, w in edges:
            adj[n1].append((n2, w))
            adj[n2].append((n1, w))
      
        #the freq map , maps, node to a freq list where each item indicate frequency of a particular weight in the path from 0 to that particular node
        freq = dict(list)
        freq[-1] = [0 for i in range(26)]
        visited = set()
        parent = [-1 for i in range(n)]
        depth_ = [-1 for i in range(n)]

        #traverese dfs, to create the freq map , depth array and parent array(for bin_lift)
        #
        def dfs(node, edge_w, par_freq, depth):
            visited.add(node)
            freq_arr = par_freq.copy()
            depth_[node] = depth
            if node != 0:
                freq_arr[edge_w-1] += 1
            freq[node] = freq_arr
            for neib, w in adj[node]:
                if neib not in visited:
                    # print(neib,node)
                    parent[neib] = node
                    dfs(neib, w, freq_arr, depth+1)
            visited.remove(node)

        dfs(0, 0, [0 for i in range(26)], 0)
        #always note to take log to  the base 2 not e 
        log_ = int(math.log2(10000))
        ance_bin_lift = [[-1 for j in range(n)] for i in range(log_+1)]
        ance_bin_lift[0] = parent.copy()

        for i in range(1, log_+1):
            for j in range(n):
                if  ance_bin_lift[i-1][j] !=-1:
                    ance_bin_lift[i][j] = ance_bin_lift[i -1][ance_bin_lift[i-1][j]]


        def lca(a, b):
            #swap nodes such that b is more deeper node from 0
            if depth_[b] < depth_[a]:
                a, b = b, a
            dist = depth_[b]-depth_[a]
            #bring up the nodes a and b to same depth 
            for i in range(log_, -1, -1):
                if (1 << i) & dist:
                    b = ance_bin_lift[i][b]
            #if they are equal , then we got the ancestor
            if a == b:
                return a
            
            #hen the remaining distance x from lca to the node (a or b) is jumped, using binary lift, 
            for i in range(log_, -1, -1):
                #this indicate we are past the lca, so not make any jump 
                if ance_bin_lift[i][a] == ance_bin_lift[i][b]:
                    continue
                #we make a jump , iff if the jumped node is below lca
                else:
                    a, b = ance_bin_lift[i][a], ance_bin_lift[i][b]
            #at then end we will be just below the lca, so return the immediate parent of this node , which is the lca
            return ance_bin_lift[0][a]
        
        # then for each query , find the lca then apply the formula
        res = []
        for q in queries:
            a, b = q[0], q[1]
            lc = lca(a, b)
            freq_arr = [0 for i in range(26)]
            #creating the freq array for path from a to b , 
            #since the freq[a] and freq[b] indicate freq of each edge weight from node 0 , 
            #the freq[lca] is repeated / common for both , that is why we need to remove it twice 
            for i in range(26):
                freq_arr[i] = freq[a][i]+freq[b][i]-2*freq[lc][i]
            ans = sum(freq_arr) - max(freq_arr)
            res.append(ans)
        return res
