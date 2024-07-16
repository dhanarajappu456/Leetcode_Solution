# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        parent = {}
        start, end   = None ,None
        def dfs(root,par):
            if root == None:
                return 
            nonlocal start,end
            
            parent[root] = par
            if root.val == startValue:
                start = root
            if root.val  == destValue:
                end  = root
            dfs(root.left,root)
            dfs(root.right,root)

        
        dfs(root,None)


        q = deque([(start,"")])

        vis  = set()
        vis.add(start.val)
        
        while(q):
            node,path  = q.popleft()
            if node == end:
                return path
            if node.left and node.left.val not in vis:
                q.append((node.left,path+"L"))
                vis.add(node.left.val)
            if node.right and node.right.val not in vis:
                q.append((node.right,path+"R"))
                vis.add(node.right.val)
            if parent[node] and  parent[node].val not in vis:
                q.append((parent[node],path+"U"))
                vis.add(parent[node].val)
            



            

        