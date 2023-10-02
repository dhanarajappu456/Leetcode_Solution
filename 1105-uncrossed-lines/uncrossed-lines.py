class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        

        '''
        this is essentially asking for the longest common subsequence
        
        
        '''

        m,n  = len(nums1), len(nums2)
        memo ={}
        def rec(i,j):

            if i<0 or j< 0:
                return 0
            if (i,j) in memo: 

                return memo[(i,j)]

            if nums1[i] == nums2[j] :

                ans =  1+ rec(i-1, j-1)
            else:

                ans  =  max(rec(i-1, j), rec(i,j-1))

            memo[(i,j)] = ans
            return memo[(i,j)]
        
        return rec(m-1, n-1)
            
