class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #msp of (col, row) mapped to the values at that position 
        map_ = defaultdict(list)
        output=[]
        def dfs(x,y,root):
            if root ==None:
                return
            
            map_[(y,x)].append(root.val)
            dfs(x+1,y-1,root.left)
            dfs(x+1,y+1,root.right)

           
        dfs(0,0,root)     
        old = float('inf')
        #sort the map based on col followed by row ,
        #then add them to the result 
        for k,v in sorted(map_.items()):
            # flag to check new column started
            if k[0]!=old:
                output.append([])
                old = k[0]
            output[-1].extend(sorted(v))
        return output  