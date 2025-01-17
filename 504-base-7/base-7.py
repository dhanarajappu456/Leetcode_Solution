import numpy as np
class Solution:
    def convertToBase7(self, num: int) -> str:
    
        base_7 = np.base_repr(num, base=7)
        return str(base_7)