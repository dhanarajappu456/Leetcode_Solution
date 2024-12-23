from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        q = deque([root])
        
        def conflict_cnt(arr):
            sorted_ = sorted(arr)
            cnt = 0
            mp = {num: i for i, num in enumerate(arr)}
            
            for i in range(len(arr)):
                while arr[i] != sorted_[i]:
                    j = mp[sorted_[i]]
                    # Swap elements
                    arr[i], arr[j] = arr[j], arr[i]
                    # Update the mapping
                    mp[arr[j]] = j
                    mp[arr[i]] = i
                    cnt += 1
         
            return cnt

        while q:
            l = len(q)
            arr = []
            for i in range(l):
                nd = q.popleft()
                if nd.left:
                    arr.append(nd.left.val)
                    q.append(nd.left)
                if nd.right:
                    arr.append(nd.right.val)
                    q.append(nd.right)
        
            cnt = conflict_cnt(arr)
            print(cnt)  # Debugging output
            ans += cnt
        
        return ans
