class Solution(object):
    def reverseWords(self, s):
        chars= list(s)
        print(chars)
        l,r = 0,len(s)-1
        while(l<r):

            chars[l], chars[r] = chars[r],chars[l]
            l+=1
            r-=1
        s ="".join(chars)
        s = s.split(" ")
        s = s[::-1]
        return " ".join(s)
       