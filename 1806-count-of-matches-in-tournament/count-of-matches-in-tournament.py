#solution1 

'''
simulation 

t = logn
s= 1




#solution 2 

observation 


the ultimate aim is to find the winner 

there are n teams and 1 winner , so n-1 teams need to be elimitated,
in each match 1 team eliminated, so to eliminate n-1 teams we need n-1 matcehs



n = 1 => ans = 0 
n = 2 => ans = 1  
n = 3 => ans = 2  
n = 4 => ans = 3  


so for n ans = n-1
t = 1
s= 1




'''
#solution 1 
# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         matches = 0
#         while(n>1 ):


#             if n%2 ==0:
#                 matches +=n//2
#                 n = n//2
#             else:
#                 matches+= (n -1 )//2 
#                 n  = (n -1 )//2 +1

#         return matches
        


#solution 2 

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1