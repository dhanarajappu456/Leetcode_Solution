from collections import deque as dq 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = dq([root])
        lev= 0
        while(q):
            n = len(q)
          
            prev = -1 if lev%2==0 else float("inf")
            for i in range(n):
                curr =q.popleft()
                if lev%2 ==0 and prev<curr.val and curr.val%2 !=0:
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                
               
                
                elif lev%2 !=0 and prev>curr.val and curr.val%2 ==0:
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                else:
                    print("ehy",curr.val,lev)
                    return False
                prev = curr.val
            lev+=1 
        return True   
                       


        