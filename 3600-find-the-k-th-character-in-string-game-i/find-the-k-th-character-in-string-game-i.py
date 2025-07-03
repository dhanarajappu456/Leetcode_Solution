class Solution:
    def kthCharacter(self, k: int) -> str:
        w  =  "a"
        while(len(w)<k):
            inter = ""
            for i in range(len(w)):
                char = chr((ord(w[i])-97 + 1)%26 +97)
                inter+= char
            w+= inter
        return w[k-1]
        