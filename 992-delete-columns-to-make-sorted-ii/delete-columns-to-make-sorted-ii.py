class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        j = 0 
        cnt = 0 
        already_sorted = [False for i in range(n)]
        #checks for each position
        while(j<m):
            i=1 
            col_deleted = False
         
            while(i<n):
                if  not(already_sorted[i]) and (strs[i][j] < strs[i-1][j]):
                    cnt+=1 
                    col_deleted = True
                    break
                i+=1
            if col_deleted:
                j+=1
                continue
            for i in range(1,n):
                already_sorted[i]|=( strs[i][j] > strs[i-1][j])
            
            j+=1


            
            
        return cnt

