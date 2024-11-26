class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        nums =  matrix
        m  = len(matrix)
        n = len(matrix[0])
        ans = 0 
        for i in range(m):
            count_neg  = 0
            min_abs_ind = 0
            min_abs_val = float("inf")
            total_row = 0
            for j in range(n):
                
                if abs(nums[i][j])<=min_abs_val:
                    min_abs_ind = j
                    min_abs_val = abs(nums[i][j])
                #change everythin to +ve
               
                if nums[i][j]<0:
                    count_neg+=1
                nums[i][j] = abs(nums[i][j])
                total_row += abs(nums[i][j])
                
            #change the min in the row to -ve  
            if count_neg%2  == 1 :
                nums[i][min_abs_ind] = -abs(nums[i][min_abs_ind])
            
            ans+= total_row
        print(ans)
        print(matrix)
        count_neg = 0 
        min_abs_val = float("inf")
        tot_neg = 0
        for j in range(n):
            
            
            for i in range(m):

                if abs(nums[i][j])<=min_abs_val:
                    min_abs_val = abs(nums[i][j])
                if nums[i][j]<0:
                    tot_neg+=1

        if tot_neg%2  == 1 :
               ans-= 2*min_abs_val

        return ans


        