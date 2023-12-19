'''
solution 1 - with additional space

for each cell find all neib's sum  and count and find ans
t mn*8
s mn


#solution 2 - without additional space

t mn*8
s 1

'''




#Solution 1 
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n  = len(img) , len(img[0])
        res =  [[ 0 for j in range(n)] for i in range(m)]

        d = [(-1,0),(1,0),(0,-1), (0,1), (-1,1),(1,-1),(-1,-1),(1,1)]
        for i in range(m):
            for j in range(n):
                tot = img[i][j]
                count =1 
                for k in range(8):
                    x,y = i+d[k][0],j+d[k][1]
                    if (0<=x<m) and (0<=y<n):
                        tot += img[x][y]
                        count+=1
                res[i][j] = math.floor(tot/count)

        return res


                               
        