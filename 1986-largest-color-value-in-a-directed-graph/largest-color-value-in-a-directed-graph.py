from collections import defaultdict as dict
#dp 
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

            if node in cycle:
                #if cycle found we need to return cycle found(true), based on which -1 is returned
                if cycle[node] ==True:
                    return True
                #if the node is not part of cycle , rather, already processed, then return the cached res
                else:
                    return memo[node]

            cycle[node] = True
            ans = [0 for i in range(26)]
            for neib in adj[node]:
                pathCol = dfs(neib)
                if  pathCol  ==  True: 
                    return True
                else:
                    #the pathCol is an array of 26 col, so lor among all paths
                    for  i in range(26):
                        ans[i] = max(ans[i] , pathCol[i])

            col   = ord(colors[node])-97
            #increment count of this current node as well by 1 
            ans[col] +=1 
            cycle[node] =False
            memo[node] = ans

            #storing the maxfreq color in the global variable
            for i in range(26):
                if ans[i]> freq[0] :
                    freq[0]= ans[i]
            return ans
            
        n =len(colors)
        for i in range(n):
            #cylce
            if dfs(i) == True:
                return -1
        #return max freq color 
        return freq[0]
            
