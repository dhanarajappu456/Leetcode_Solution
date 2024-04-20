# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        m = defaultdict(list)
        max_h  = 0
        def rec(root,h):
            nonlocal max_h
            if root == None:
                return 
            if root.left  == None and root.right == None and h>=max_h :
                if h>max_h:
          
                    if max_h  in m:
                        m.pop(max_h)
                    max_h = h
                m[max_h].append(root.val)
                return 
       
            rec(root.left,h+1)
            rec(root.right,h+1)
        rec(root,0)
        return sum(m[max_h])