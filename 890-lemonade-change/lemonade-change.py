class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        #on_counter keeps the changes present in counter
        #to_pay is the payment to be done to the people

        on_counter = defaultdict(int)
        to_pay = defaultdict(int)
        for bill in bills:
            debt  = bill - 5
            on_counter[bill]+=1
            if debt>0:
                if (debt == 5) :
                    if( on_counter[debt] >= 1):
                        on_counter[debt]-=1 
                        
                    else:
                        return False
                    
                if (debt == 15 ):
                    if ((on_counter[10]>=1)  and ( on_counter[5]>=1)) :
                        on_counter[10]-=1
                        on_counter[5]-=1

                    elif ( on_counter[5]>=3):
                        on_counter[5] -= 3

                    else:
                        return False
        return True


            
                
            
            

        