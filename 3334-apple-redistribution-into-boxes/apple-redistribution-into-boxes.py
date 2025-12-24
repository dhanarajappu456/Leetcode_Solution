class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse  = True )
        tot_app  = sum(apple)
        #print(tot_app)
        i  = 0 
        s =  0
        n  = len(capacity)
        while((i<n) and (s < tot_app)):
            s+=capacity[i]
            #print("sd",s)
            i+=1
        return i


            