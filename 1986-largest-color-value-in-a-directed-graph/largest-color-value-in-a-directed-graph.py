from collections import defaultdict as dict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:


        cycle  ={}
        memo= {}
        adj = dict(list)
        for s, e in edges:
            adj[s].append(e)
          

        res = [0]
        freq = [0]

        def dfs(node):
            #print(node,memo,"\n")
            if node in cycle:
            
                if cycle[node] ==False:
                    return memo[node]
                else:
                    print("cy",node)
                    return True
            cycle[node]= True
        
            ans =[0 for i in range(26)]
            for neib in adj[node]:
                pathCol = dfs(neib)
                if  pathCol  ==  True: 
                    return True
                else:
                    for  i in range(26):
                        ans[i] = max(ans[i] , pathCol[i])
            
            col   = ord(colors[node])-97
            ans[col] +=1 
            cycle[node] =False
            memo[node] = ans
            for i in range(26):
                if ans[i]> freq[0] :
                    res[0] =i
                    freq[0]= ans[i]
            return ans
        n =len(colors)
        for i in range(n):
            if dfs(i) == True:
                return -1
        #print(res[0],freq[0])
        return freq[0]
            
