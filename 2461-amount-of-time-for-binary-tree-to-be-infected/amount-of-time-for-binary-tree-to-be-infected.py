# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
crate adj list (including parent )

then do bfs 

t n 
s n(stack space and vis and queue)

'''
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:


        def rec(root,par):
            nonlocal start
            if root == None:
                return 
            
            parent[root] = par
            if root.val == start:
                start = root
            rec(root.left, root)
            rec(root.right, root)

        parent = dict()
        rec(root,-1)
        q = deque([start])
        min_time = -1
        vis  = set()
        vis.add(start.val)
        while(q):
            
            min_time+=1 
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if parent[node] !=-1 and  parent[node].val not in vis:
                    q.append(parent[node])
                    vis.add(parent[node].val)
                if node.left!= None and node.left.val not in vis:
                    q.append(node.left)
                    vis.add(node.left.val)
                if node.right!= None and node.right.val not in vis:
                    q.append(node.right)
                    vis.add(node.right.val)
        return min_time
                    

                

            
        
