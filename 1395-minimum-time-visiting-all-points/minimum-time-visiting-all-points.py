class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:


        time = 0
        n  =len(points)
        for i in range(1,n): 

            time  = time+ max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return time