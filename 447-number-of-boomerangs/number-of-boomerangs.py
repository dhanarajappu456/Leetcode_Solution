class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        def dist(a,b):
            x1,y1 = a
            x2,y2 = b

            return (x2-x1)**2 + ( y2-y1)**2

        ans  =0 
        n  = len(points )
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,n):
                   
        #             if abs(dist(points[i],points[j]) == dist(points[i],points[k])):
        #                 ans+=2
        #             if abs(dist(points[j],points[k]) == dist(points[j],points[i])):
        #                 ans+=2
        #             if abs(dist(points[k],points[i]) == dist(points[k],points[j])):
        #                 ans+=2
        # return ans
        m = defaultdict(lambda : defaultdict(int))
        for i in range(n-1):
            for j in range(i+1,n):
                d = dist(points[i],points[j])
                m[(points[i][0],points[i][1])][d]+=1
                m[(points[j][0],points[j][1])][d]+=1

        for p in m :
            for d in m[p]:
                c = m[p][d]
                if c>=2:
                   
                    ans+= math.factorial(c)/(math.factorial(c-2)*math.factorial(2))

        return int(ans)*2
        
                            
        