class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n  = len(letters)
        for i in range(n):
            c = letters[i]
            if c <= target:
                i+=1
            else:
                break
        return letters[i] if i<n else letters[0]
        


