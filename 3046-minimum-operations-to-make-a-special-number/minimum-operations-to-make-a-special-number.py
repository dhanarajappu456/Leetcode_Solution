class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        def func(x, y):
            first = num.rfind(x)
            if first == -1:
                return n 
            second = num.rfind(y, 0, first)
            if second == -1:
                if x =="0":
                    zeros =0 
                    for i in range(n):
                        if num[i]=="0":
                            zeros+=1
                    return n-zeros
                else:
                    return n 
            print(first, second,first - second -1 ,  n-1-  first)
            return first - second -1 +  n-1-  first
        _00 = func('0', '0')
        _25 = func('5', '2')
        _50 = func('0', '5')
        _75 = func('5', '7')
        
        return min(n,_00,_25,_50,_75)
    
    

            
        