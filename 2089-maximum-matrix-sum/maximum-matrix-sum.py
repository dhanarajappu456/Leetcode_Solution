class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt  = 0 
        cnt_neg = 0 
        tot_sum = 0
        min_abs_val = float("inf")
        for arr in matrix:
            row_neg = 0 
            for n1 in arr:
                if n1<0:
                    row_neg +=1 
                tot_sum+= abs(n1)
                min_abs_val  = min(min_abs_val, abs(n1))
            if row_neg%2 ==1:
                cnt_neg +=1
        #if number pf rows in  which odd number of neg number exist is odd 
        if cnt_neg%2 ==1:
            return tot_sum  - 2*min_abs_val
        else:
            return  tot_sum

        
        

        if cnt%2==1:
            return tot_sum-1
        return tot_sum


        
        