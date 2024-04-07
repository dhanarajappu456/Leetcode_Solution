"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        # print(root.children )
        # return []
        ans = []
        def rec(node):

            if root == None:
                return
            
            ans.append(node.val)
            for c in node.children:
                rec(c)
        rec(root)
        return ans