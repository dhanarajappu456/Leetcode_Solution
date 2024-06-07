class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:


        dictionary = set(dictionary)
        ans  = []
        for w in sentence.split(" "):
            added = False
            for i in range(len( w)):
                if w[:i+1] in dictionary:
                    added   = True
                    ans.append(w[:i+1])
                    break
            if not(added):
                ans.append(w)
                
        return " ".join(ans)