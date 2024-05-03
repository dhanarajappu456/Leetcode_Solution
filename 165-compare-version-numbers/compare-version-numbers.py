class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        l1,l2 =  version1.split("."),version2.split(".")
        m,n = len(l1), len(l2)
        print(l1,l2)
        i,j = 0, 0
        while(i<m and j<n):
            print(l1[i],l2[j],int(l1[i]) ,int(l2[j]))
            if int(l1[i])> int(l2[j]):
                return 1
            elif int(l1[i])< int(l2[j]):
                return -1 
            i+=1
            j+=1

        while(i<m):
         
            if int(l1[i])!=0:
                return 1
            i+=1
    

        while(j<n):
         
            if int(l2[j])!=0:
                return -1
            j+=1
        return 0
        