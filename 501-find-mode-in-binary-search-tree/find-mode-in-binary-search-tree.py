from collections import defaultdict as dict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        count = dict(int)
        li =[]
        top = 0
        def rec(root):

            if root ==None:
                return 
            nonlocal top;
            li.append(root.val)
            count[root.val]+=1
            if count[root.val]>top:
                top = count[root.val]

            rec(root.left)
            rec(root.right)
        
        rec(root)
      
        ans =[]
        for item in count:
            if count[item] == top: 
                ans.append(item)
        return ans 
        