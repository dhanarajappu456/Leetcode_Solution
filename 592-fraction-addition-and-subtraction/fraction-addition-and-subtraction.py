import math as m 

class Solution:
    def fractionAddition(self, expression: str) -> str:

        n = len(expression)
        i=0 
        # previous numerator and denominator 
        numerator = 0
        denominator = 1
        while(i<n):
            isNeg = False
            #current numerator and denominator
            curr_num,curr_deno = 0,0
            val  = expression[i]
            #checking if current expression is negative 
            if val ==  "-":
                isNeg = True
            if val in ["+", "-"]:
                i+=1
            #building current numerator
            while(i<n and expression[i].isdigit()):
                curr_num =  (curr_num * 10) + int( expression[i])
                i+=1
            i+=1 

            #building the negative number
            if isNeg :
                curr_num *= -1
            #building current denominator
            while(i<n and expression[i].isdigit()):
                curr_deno  = (curr_deno * 10 ) + int( expression[i])
                i+=1
            # stroring the numerator and denominator 
            numerator = numerator*curr_deno + denominator*curr_num
            denominator = curr_deno *denominator

           
        #finding gcd and simplifying the fraction
        gcd_ = m.gcd(numerator, denominator)
        numerator  = numerator // gcd_
        denominator  = denominator // gcd_
        return(str(numerator) + "/" +str(denominator))

      