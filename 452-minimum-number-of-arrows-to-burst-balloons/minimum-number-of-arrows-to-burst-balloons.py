class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        cnt = 0
        i = 0
        n =len(points)
 
        while(i<n):
            
            j = i
            min_x_end = points[i][1]
            while(j<n and points[j][0]<=min_x_end):
                min_x_end = min(min_x_end,points[j][1])
                j+=1
            i=j
            cnt+=1
        return cnt
                
        