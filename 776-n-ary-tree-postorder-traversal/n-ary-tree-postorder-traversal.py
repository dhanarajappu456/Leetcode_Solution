"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stk = []
        
        if root:
            stk = [root]
        ans  = []
        while(stk):
            root = stk.pop(-1)
            ans.append(root.val)
            for c in root.children:
                stk.append(c)
        return ans[::-1]



        