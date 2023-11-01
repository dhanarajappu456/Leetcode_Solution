from collections import defaultdict as dict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        count = 0
        max_ = 0
        prev = 10**5 + 1

        def rec(root):
            if root is None:
                return
            nonlocal count, max_, prev, ans 
            rec(root.left)
            if prev == root.val:
                count += 1
            else:
                count = 1
            if count == max_:
                ans.append(root.val)
            elif count > max_:
                ans = [root.val]
                max_ = count
            prev = root.val
            rec(root.right)

        rec(root)
        return ans
