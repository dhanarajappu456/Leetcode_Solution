class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n  = len(img) , len(img[0])
        sum_, count = [[img[i][j] for j in range(n)] for i in range(m)], [[1 for j in range(n)] for i in range(m)]

        d = [(-1,0),(1,0),(0,-1), (0,1), (-1,1),(1,-1),(-1,-1),(1,1)]
        for i in range(m):
            for j in range(n):
                for k in range(8):
                    x,y = i+d[k][0],j+d[k][1]
                    if (0<=x<m) and (0<=y<n):
                        sum_[i][j] += img[x][y]
                        count[x][y]+=1 
    
        

        for i in range(m):
            for j in range(n):

                sum_[i][j] = math.floor(sum_[i][j]/count[i][j])

        return sum_



                               
        