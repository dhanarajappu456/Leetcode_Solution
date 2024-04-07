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
        stk =[]
        if root:
            stk =[root]

        while(stk):

            node =stk.pop(-1)
            ans.append(node.val)
            for c in node.children[::-1]:
                stk.append(c)
            
        return ans