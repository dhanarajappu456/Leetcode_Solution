class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        locked_op , non_locked =   [] ,[]
        for i, c in enumerate(s):
            if locked[i] =="1":
                if c ==")":
                    if locked_op:
                        locked_op.pop(-1)
                    elif non_locked:
                        non_locked.pop(-1)
                    else:
                        return False
                else:
                    locked_op.append(i)
            else:
                non_locked.append(i)
        
        while(locked_op and non_locked and non_locked[-1]> locked_op[-1]):
            locked_op.pop(-1)
            non_locked.pop(-1)
        print(locked_op,non_locked)
        return  (locked_op ==[] )and (len(non_locked) %2 ==0)

        
                    
                        
        