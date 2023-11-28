'''


question is simple , when we first find 2 seats , then following plants can form different partition with this seat, 
that is why we do ans*(p+1) ,

but there could be situatiuo  when we cant find 2 seats only 1 seat isw found , and we exhauseted the array , in that case  just return 0 

also remember when a set of plants after 2 seats are found this can form differnet partition with this 2 seat, there another seat following the grp of plants , else , this grp of plant can form a single partition with the grp of the last chosen 2  seats

you can start iterating either from beginning or end, here we start from end


'''
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        mod= 10**9+7
        n = len(corridor)
        s=0
        ans = 1
        i= n-1
        s,p=0,0

        
        while(i>=0 ):
            
            #finding a grp of 2 seats 
            while(i>=0 and s!=2):
                if corridor[i]=="S":
                    s+=1

                i-=1
            #no 2 seats can be found only a single seat is found, so no valid parition possible 
            if i<0 and  s!=2: 
                return 0
            
            #finding grp of plants that can form different parition , with last chosen grp of 2 seats
            while(i>=0  and s==2):
                if corridor[i]=="P":
                    p+=1
                #in case currnt is a seat just break , as we are intreseted in plants here
                else:
                    break

                i-=1
            #the plants we got after 2 seats can from different partition iff ,  there is a seat followinf the grp of plant , else we
            #can have only 1 parition (p=0 then p+1 =1 ) with this grp of plants
            if i<0:
                p =0
            ans  *= (p+1)
       
            s,p =0,0


        
        

        return ans%mod

        