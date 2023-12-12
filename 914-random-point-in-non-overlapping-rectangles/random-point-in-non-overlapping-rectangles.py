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

'''
using cumulative freq and bin search 

since we need the probavility to be eqully likely, we  have more probaility to find a point in a reactangle that has 
greater number of points

so we store the , the cumulative freq based on the number of points in each rectangle, 
then we find a random number b/w 1 and entire number of points in the entire rectangle. 
based on which we find the rectangle in which this point fall in 

and return it 


'''
import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):

        self.rects = rects
        #each index denote the rectangles index and  cumulative freq(number of points ) ,upto the rectangle
        self.cum_freq=[]
        
        self.totPoints= 0 

        #generate the cumulative freq , using number of points 
        for rect in rects:

            bx,by,tx,ty = rect

            self.totPoints +=  (tx-bx+1)*(ty-by+1)

            self.cum_freq.append(self.totPoints)

    def pick(self) -> List[int]:
        #generate random number 
        rand_val = random.randint(1,self.totPoints)
        #find the  index of rectanfgle to which this freq fall to 
        ind  = bisect.bisect_left(self.cum_freq , rand_val)
        rect = self.rects[ind]
        x,y = random.randint(rect[0],rect[2]) , random.randint(rect[1],rect[3])
        return [x,y]





