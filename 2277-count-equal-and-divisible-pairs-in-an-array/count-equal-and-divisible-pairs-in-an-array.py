from collections import defaultdict as dict
from math import gcd
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        #1.make not of all the factors of k
        #2.create a map that maps each number to its indices of occurences
        #3. for each number , we gonna find the pairs using math trick of gcd
        #a. we do this by iterating on the list of indices of eahc number from the map
        #suppose we are at index value i , then we calcualte , gcd(i,k)
        #which x = k/gcd(i,k) gives a number that factored out factors of of i and k 
        #from k and , now x is the "needed" factor of k , so any number  j that is 
        #multiple  of this "needed" thus forms the pair with i , giving , i*j 
        #as the multiple of k
        #for this to work efficiently , we need to store  a map where the 
        #factors of k is mapped to the numbers (j) which are multiple of 
        #of those factors , this is done in mp




        n = len(nums)
       
        factors = set()
        val_ind = dict(list)
        #factors of k 
        for i in range(1,k+1):
            if k%i == 0:
                factors.add(i)
        #creating num -> [indices list]
        for i,num in enumerate(nums):
            val_ind[num].append(i)
        ans = 0 
        for num in val_ind:
            mp  = dict(int)
            
            for i in val_ind[num]: 

                needed  = k//gcd(i,k)
                #number of j previously visited , that form pair with
                #current index i
                ans+=mp[needed]
                #counting this i as  multiple of all the fact
                #that divides it
                for fact in factors:
                    if i%fact ==0:
                        mp[fact]+=1
        return ans
                

        
        

        

        