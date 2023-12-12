'''
Solution 1 - Memory limit exceeded 

bruteforce, store all the points of each reactangle into an array 
and take random point out of that

t 10^4(assuming random.choice takes o(1))
s 100 *(2000*2000)


'''
#solutiion 1 
import random 

# class Solution:

#     def __init__(self, rects: List[List[int]]):
        
#         self.points= []
#         for rect in rects:
#             bx,by,tx,ty = rect
           
#             for x in range(bx,tx+1):
#                 for y in range(by,ty+1):

#                     self.points.append((x,y))
        
      

            

#     def pick(self) -> List[int]:
#         n= len(self.points)
#         return random.choice(self.points)
        


#solution 2 

import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):

        self.rects = rects
        self.points=[]

        self.totPoints= 0 

        for rect in rects:

            bx,by,tx,ty = rect

            self.totPoints +=  (tx-bx+1)*(ty-by+1)

            self.points.append(self.totPoints)

    def pick(self) -> List[int]:
        rand_val = random.randint(1,self.totPoints)
        ind  = bisect.bisect_left(self.points , rand_val)
        rect = self.rects[ind]
        x,y = random.randint(rect[0],rect[2]) , random.randint(rect[1],rect[3])
        return [x,y]





