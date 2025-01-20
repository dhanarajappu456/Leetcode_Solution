class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # 1.create the map that maps , the val to (i,j)
        #2.for each value iterated over the arr mark a value visited
        #in the corresponding col and row .
        #3.at any point , when any row or col is completely visited, return 
        #that col or row
        val_ind = {}
        cols_rem = {}
        rows_rem = {}
        
        m,n = len(mat), len(mat[0])
        #this map indicate , the number of univisted elements
        #in each col
        for j in range(n):
            cols_rem[j] = m
        #this map indicate , the number of univisted elements
        #in each row
        for i in range(m):
            rows_rem[i] = n
        
        #creating the map that maps , val-> (i,j)
        for i in range(m):
            for j in range(n):
                val_ind[mat[i][j]] = (i,j)

        #when each val is visited in mat , corresponding row and col
        #is marked (by decrementing the number of unvisited value in
        #each of them)   
        for k in range(len(arr)):
            val  = arr[k]
            i,j = val_ind[val]
            rows_rem[i] -=1
            cols_rem[j]-=1
            if( rows_rem[i] == 0 ) or (cols_rem[j] == 0):
                return  k
        
