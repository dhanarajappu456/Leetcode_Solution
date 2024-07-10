class Solution:
    def minOperations(self, logs: List[str]) -> int:

        folds = 0
        for op in logs:
            if op =="../":
                if folds:
                    folds-=1
            elif op!="./":
                folds+=1
 
        return folds

        