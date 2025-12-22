class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        j = 0 
        cnt = 0 
        #already_sorted[i] tells if the strs[i] and strs[i-1] is sorted or not
        already_sorted = [False for i in range(n)]
        #checks for each position
        while(j<m):
            i=1 
            #flag for knowing if the current col is deleted
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
            #stroting the info if the strs[i] and strs[i-1] is sorted
            #remeber we din stroe this information while traversing the strings in whti while i<n loop
            #cuz there will be case where we stored it for  and index i , but for indexx > i we  come to know the the column j is entirely deleted in future 
            # so we need the chnages , that is why we mark it at end of the loop , if the col_deleted = false
            for i in range(1,n):
                already_sorted[i]|=( strs[i][j] > strs[i-1][j])
            
            j+=1


            
            
        return cnt

