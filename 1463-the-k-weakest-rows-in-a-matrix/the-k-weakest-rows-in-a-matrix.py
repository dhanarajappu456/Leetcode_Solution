class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:


        m,n  = len(mat), len(mat[0])

        arr =[]
        for i in range(m): 
            arr.append((mat[i].count(1),i))
        print(arr)
        arr.sort()
        return [ind  for count  ,ind in arr[:k]] 


        