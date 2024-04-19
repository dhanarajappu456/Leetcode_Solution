"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def rec(root):
            if root == None:
                return 0
            max_depth =  0
            for c in root.children:
                max_depth  = max(max_depth,rec(c))
            
            return max_depth + 1
        return rec(root)