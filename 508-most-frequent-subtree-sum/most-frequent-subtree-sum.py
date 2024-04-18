# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict as dict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        m = dict(int)
        freq = 0
        def rec(root):
            nonlocal freq
            if root == None:
                return 0 
            s = root.val + rec(root.left) +rec(root.right)  
            m[s]+=1
            if m[s]>=freq:
                freq =m[s]
            return s
        rec(root)
        ans = []
        for s in m:
            if m[s] == freq:
                ans.append(s)
        return ans