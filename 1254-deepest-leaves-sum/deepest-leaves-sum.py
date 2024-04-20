# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        visited = set()
        queue = deque([root])
        visited.add(root)
        ans =0
        while queue:
            n =len(queue)
            ans  = 0 
            for i in range(n):
                node = queue.popleft()
                ans+= node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
