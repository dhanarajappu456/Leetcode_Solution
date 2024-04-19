"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque([])
        if root:
            q.append(root)
            
        res =[]
        while(q):
            n = len(q)
            ans  =[]
            for i in range(n):
                node = q.popleft()
                for c in node.children:
                    if c :
                        q.append(c)
                ans.append(node.val)
            res.append(ans)
        return res



        