class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        cnt = 0
        i = 0
        n =len(points)
        print(points)
        while(i<n):
            
            j = i
            highest_range_right = points[i][1]
            while(j<n and points[j][0]<=highest_range_right):
                highest_range_right = min(highest_range_right,points[j][1])
                j+=1
            i=j
            cnt+=1
        return cnt
                
        