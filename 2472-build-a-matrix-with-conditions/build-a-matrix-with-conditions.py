class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        #create the toposort on col and rows
        #for each value based on the position obtained from toposort , fill the matrix
        n  = k
        ans = [[0 for i in range(k)] for j  in range(n)]
        adj1  = defaultdict(list)
        adj2 = defaultdict(list)
        indeg_row, indeg_col =[0 for i in range(k+1)],[0 for i in range(k+1)]


        for a,b in rowConditions: 
            adj1[b].append(a)
            indeg_row[a]+=1
        for a,b in  colConditions: 
            adj2[b].append(a)
            indeg_col[a]+=1
        
        def rec(root,adj,res):
            if  root in path:
                return True
            if root in vis:
                return False
            path.append(root)
            vis.add(root)
         
            for nb in adj[root]:
                if rec(nb,adj,res):
                    return True
            
            res.append(root)
            path.pop(-1)


     
        row,col  = [],[]
        #print(indeg_row,indeg_col)

  
        vis = set()
        path = []
        for val in range(1,k+1):
          
            if rec(val,adj1,row):
                return []
            
        vis = set()
        path= []
        for val in range(1,k+1):
 
            if rec(val,adj2,col):
                return []
        

        pos_row,pos_col = defaultdict(int),defaultdict(int)

        for i in range( k):

            pos_row[row[i]] = i
            pos_col[col[i]] = i 
    
        for val in range(1,k+1):
            r,c  = pos_row[val],pos_col[val]
            ans[r][c] = val
        
        return ans

        