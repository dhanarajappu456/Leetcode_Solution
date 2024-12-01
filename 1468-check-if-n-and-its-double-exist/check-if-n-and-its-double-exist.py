class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnts = Counter(arr)
        for num in cnts:
            if 2*num in arr:
                if (num  == 0 and cnts[0]>1) or (num!=0):
                    return True
        return False
        