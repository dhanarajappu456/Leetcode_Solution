# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        ans  =  0
        q = deque([root])
        def conflict_cnt(arr):
            sorted_ = sorted(arr)
            cnt =  0 
            mp = { num : i for i,num in enumerate(arr)}
      
            for i in range(len(arr)):
                if arr[i]!= sorted_[i]:
                    #put correct element at i , by swwpping
                    j = mp[sorted_[i]]
                    arr[i] , arr[j] =  arr[j] , arr[i]
                    cnt+=1
                    #update the mp, after swapping
                    mp[arr[i]] = i 
                    mp[arr[j]] = j
          
         
            return cnt

        while(q):
            l = len(q)
            arr =[]
            for i in range(l):
                nd = q.popleft()
                if nd.left:
                    arr.append(nd.left.val)
                    q.append(nd.left)
                if nd.right:
                    arr.append(nd.right.val)
                    q.append(nd.right)
        
            cnt   = conflict_cnt(arr)
            print(cnt)
            ans += cnt
        return ans 