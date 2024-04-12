class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])
        arr = [ deque([]) for i in range(m+n-1)]
  
        for i in range(m):
            for j in range(n):
                if (i+j)%2 !=0:
                    arr[i+j].append(mat[i][j])
                else:
                    arr[i+j].appendleft(mat[i][j])
     
        ans  = []
        for a in arr:
           
            for v in a:
                ans.append(v)
        return ans