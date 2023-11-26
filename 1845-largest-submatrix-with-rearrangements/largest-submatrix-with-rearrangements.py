'''
starting from the base, we calculate the heights of each builiding in the column(in a consecutive, cumulative fashon)
at at any row, we thus have  building heights , in each column ending at that row or a value of 0 ,
 now since we can rearrange column
 that is heights. to get the max height , we need to follow a greedy way , which is sorting the heghts in increading 
 order so that , wach building at a column can form a submatrix with all heights to right of it 

'''
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        '''
        t  mnlogn
        s  n

        '''
        m,n   = len(matrix) , len(matrix[0])
        heights =[0 for i in range(n)]
        max_area = 0


        for i in range(m-1,-1,-1):

            for j in range(n):

                if matrix[i][j] ==  0:
                    heights[j] = 0 
                else:
                    heights[j]+=1
            #remeber we need to sort on the copy of heights
            sortedHeights = sorted(heights)
            for j in range(n):
                h = sortedHeights[j]
                area = h*(n-j)
             
                max_area = max(area,max_area)
         
        return max_area



