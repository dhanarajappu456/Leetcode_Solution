class Solution(object):
    def reverseWords(self, s):
        words= s.split(" ")
        res =[ ]
        for w in words:

            rev= ""
            for c in w[::-1]:
                rev+= c
            res.append(rev)

        print(res)


        return " ".join(res)

        