class Solution:
    def kthCharacter(self, k: int) -> str:
        index = k-1
        set_bits  = 0
        while(index):
            if index & 1:
                set_bits+=1
            index>>=1
        return chr(set_bits + 97)