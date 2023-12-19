'''
solution 1 - with additional space

for each cell find all neib's sum  and count and find ans
t mn*8
s mn


#solution 2 - without additional space- using bits(inplace)

when we are at a cell 
we store the value in the cell such that , 8 lsb(since img[i][j] can at max be 255 ,) for the value that was in the cell before
and the next msbs to store the actual ans , 
thus each cell stores both the final ans and the value that was at the location earlier

t mn*8
s 1

'''




#Solution 2
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
                        #retrive the earlier value that was at img[i][j]
                        #which is last 8bits
                        tot += img[x][y]%256
                        count+=1
                #store the result  followed by the actual value that was  at the img[i][j]
                img[i][j] = ( (math.floor(tot/count) <<8) | img[i][j] )

        #retireive the result 
        for i in range(m):
            for j in range(n):
                #tha ans is represented by next bits after removeing  8lsb 
                img[i][j] = img[i][j]>>8
        return img


                               
        