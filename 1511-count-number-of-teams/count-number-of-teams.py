class Solution:
    def numTeams(self, rating: List[int]) -> int:

      
        ans =0 
        n  = len(rating)
        for j in range(1,n-1):
            
            left_smalls,left_greats,right_smalls,right_greats =0,0,0,0
            n2 = rating[j]

            #finding cnt of nums on left side, < n2  (middle element)
            #and also cnt of nums on left side> n2 
            for i in range(j):
                if rating[i]<n2:
                    left_smalls+=1
                if rating[i]>n2:
                    left_greats+=1
            
            #finding cnt of nums on right side, < n2  (middle element)
            #and also cnt of nums on right side> n2 
            for k in range(j+1,n):
                if rating[k]<n2:
                    right_smalls+=1
                if rating[k]>n2:
                    right_greats+=1
            #the final ans is 
            #combination 1  - smalls on left , n2 , large on right
            #combination 2 -  large on right, n2, small on right
            ans += left_smalls *right_greats  + left_greats * right_smalls
            
        return ans
        