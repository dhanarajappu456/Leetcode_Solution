class ListNode:
    def __init__(self,key=0,val=0):
        
        self.key  = key
        self.val = val
        self.next =None 

class MyHashMap:

        
    def __init__(self):
        #load factor must be lesse than 0.75 , therefore we choose the nummber of bucket , 15000
        self.n= 15000
        self.hash = [ ListNode(0,0) for i in range(15000)]
        

    def put(self, key: int, value: int) -> None:
        
        index = self.hashFunc(key)
        
        curr= self.hash[index]
        
        while(curr.next): 
            #if the key already present then , update the existing node key's valur
            if curr.next.key == key:
                curr.next.val  = value
                return
            curr = curr.next
        curr.next = ListNode(key,value )
        

    def get(self, key: int) -> int:
        
        index = self.hashFunc(key)
        
        curr= self.hash[index].next
        
        while(curr): 
            #return the value  if the key present
            if curr.key == key:
                return curr.val 
            curr = curr.next
        
        return -1
    
        

    def remove(self, key: int) -> None:
        
        index = self.hashFunc(key)
        
        curr= self.hash[index]
        
        while(curr.next): 
            #if key presen then just delete the node , by reassigning the links
            if curr.next.key == key:
                curr.next = curr.next.next
                break
            curr = curr.next
    def hashFunc(self,key):
        return key%self.n 
        
    

    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)