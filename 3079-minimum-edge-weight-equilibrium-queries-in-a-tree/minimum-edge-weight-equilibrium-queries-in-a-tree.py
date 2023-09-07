from collections import defaultdict as dict

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        #create adjlist 
        adj  = dict(list)
        for n1,n2,w in edges:
            adj[n1].append((n2,w))
            adj[n2].append((n1,w))
        #traverse dfs, from  to parent array
        freq =dict(list)
        freq[-1] = [0 for i in range(26)]
        visited = set()
        parent  =[-1 for i in range(n)]
        depth_ = [-1 for i  in range(n)]
        #print(adj)
        def dfs(node,edge_w,par_freq,depth):
            visited.add(node)
            freq_arr = par_freq.copy()
            depth_[node]= depth
            if node!=0:
                
                freq_arr[edge_w-1]+=1
            freq[node]=freq_arr
            for neib,w in adj[node]:
                if neib not in visited:
                    #print(neib,node)
                    parent[neib] = node
                    dfs(neib,w,freq_arr,depth+1)
            visited.remove(node)
        dfs(0,0,[0 for i in range(26)],0)
        #print(parent,freq,depth_)



        #while doing this dfs, also fill up the frequcny array for each node
        #after getting the parent array , build the binary lift matrix
        log_ = int(math.log2(10000))
        ance_bin_lift = [[ -1 for j in range(n)] for i in range(log_+1)]
        ance_bin_lift[0] = parent.copy()

        for i in range(1,log_+1):
            for j in range(n):
                if 0 <= ance_bin_lift[i-1][j] < n:
                    ance_bin_lift[i][j] = ance_bin_lift[i-1][ance_bin_lift[i-1][j]]

        #print(ance_bin_lift)

        def lca(a,b):


            if depth_[b]<depth_[a]:
                a,b  = b,a

            dist  = depth_[b]-depth_[a]
            #print(dist)
        
            for i in range(log_,-1,-1):
                if (1<<i)&dist:
                    b = ance_bin_lift[i][b]
            if a==b:
                return a
            
            for i in range(log_,-1,-1):

                if ance_bin_lift[i][a] ==ance_bin_lift[i][b]:
                    continue
                else:

                    
                    a,b = ance_bin_lift[i][a], ance_bin_lift[i][b]
                
            
            return ance_bin_lift[0][a]
        # then for each query , find the lca then apply the formula
        
        
        res=[]
        for q in queries:
     
            a,b  = q[0],q[1]
            lc =lca(a,b)
            freq_arr =[0 for i in range(26)]
            #print(a,b,lc , freq[a],freq[b],freq[lc])
            for i in range(26):
                #print(freq[a][i],freq[b][i],2*freq[lc][i])
                freq[a][i]
                freq[b][i]
                #print(lc)
                2*freq[lc][i]
                freq_arr[i] = abs(freq[a][i]+freq[b][i]-2*freq[lc][i])
            #print(freq_arr)
            ans  = sum(freq_arr) - max(freq_arr) 
            res.append(ans)
        return res



        
        
        





            






       
        




        
        