'''
solution 1 
generate the random numbers and see if it is in  the blacklist , if yes retry generating 
else return the number directly

t this is not efficient , as for each pick we dont know when we get the whitelist number
s 1 

solution 2 -using hash map 

the idea is if we have all the black list number at the  end , then we can generate random numb from (0,k-1) ,
where k is the length of whitelist numbers  and k = n-len(blacklist)


but it maynot be the case always , there may be some numbers <=k-1 that is a blacklist number , in that case we cant directly return random number generated, 

for this we map thes values <=k-1 to whitelist numbers>=k

and when we generate a randmo number  from [0,k-1] ,we see if it a blacklist and its mapped number from the mapping

t  creating mapping len(blacklist) 
s  len(blacklist)

'''

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        #length(k) which is number of whitelist numbers 
        self.white_len   = n  - len(blacklist) 
        #these are numbers >=k, which are whitelist that need to be mapped to numbers <=k-1
        self.whites_to_move = []


        for i in range(self.white_len, n):
            if i not in blacklist:
                self.whites_to_move.append(i)

        j = 0
        self.mapping ={}
        #creating mapping 
        #map contain
        # (blackilist numbers<=k-1 )-> (whitelist number >=k )
        for i in blacklist:
            if i<self.white_len:
                self.mapping[i] =self.whites_to_move[j]
                j+=1
             
    def pick(self) -> int:
        val = random.randint(0,self.white_len-1)
        #if the number is blacklist then , return the mapped whitelist number
        if val in self.mapping:
            return self.mapping[val]
        
        return val
