class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''

        since can go through x y and diag direction with 1 unit of time per step ,


        to reach from p1 to p2 , we need to travel max distance wchich is either the diff in x coord of p1 and p2 or 
        diff in y coord of p1 and p2

        t n 
        s 1
        '''

        time = 0
        n  =len(points)
        for i in range(1,n): 

            time  = time+ max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return time