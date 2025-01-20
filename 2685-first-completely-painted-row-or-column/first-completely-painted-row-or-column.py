class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        '''
        solution 2 - space optimised little ,
        If we store the  index of each val in the arr
        in a map, 
        1.then we can iterate over each row to see , what's the 
        max ind in arr at which entire element of that row 
        is marked visited
        2.similary we can iterate over each col to see , what's the
        max ind in arr at which entire elements in that col is marked
        as visited




        '''
        val_ind = {}
        
        ans  = len( arr)-1
        m,n = len(mat), len(mat[0])
        #maps each val to their ind in arr
        for j in range(len(arr)):
            val  = arr[j]
            val_ind[val]  = j 
        #for each row see max ind in arr , at which entire row is marked
        for i in range(m):
            max_ind  = 0 
            for j in range(n):
                val  = mat[i][j]
                max_ind = max(max_ind , val_ind[val])
            ans = min(ans, max_ind)
        for j in range(n):
            max_ind  = 0 
            for i in range(m):
                val  = mat[i][j]
                max_ind = max(max_ind , val_ind[val])
            ans = min(ans, max_ind)
                
        return ans
       