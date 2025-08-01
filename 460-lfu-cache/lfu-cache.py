from collections import defaultdict as dict, OrderedDict as ordD
class LFUCache:
    def __init__(self, capacity: int):
        self.keyFreqMap = dict()
        self.freqKeyMap = dict(ordD)
        self.minFreq = 0
        self.capacity  = capacity 

    def get(self, key: int) -> int:        
        if key in self.keyFreqMap:
            oldFreq = self.keyFreqMap[key]
            val  = self.freqKeyMap[oldFreq][key]
            #update the freq
            newFreq = oldFreq+1
            self.keyFreqMap[key] = newFreq
            
            #remove the key from olf freq dictionary and insert into new freq dict
            self.freqKeyMap[ oldFreq].pop(key)
            self.freqKeyMap[ newFreq][key]= val 
            #update the minfreq
            if self.minFreq == oldFreq and len(self.freqKeyMap[ oldFreq])==0:
                self.minFreq =newFreq
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        #key present then upddate it in the key dicitonnary and freq dectionary
        if key in self.keyFreqMap:
            oldFreq = self.keyFreqMap[key]
            val  = self.freqKeyMap[oldFreq][key]
            #update the freq
            newFreq = oldFreq+1
            self.keyFreqMap[key] = newFreq
            
            #remove the key from olf freq dictionary and insert into new freq dict
            self.freqKeyMap[ oldFreq].pop(key)
            self.freqKeyMap[ newFreq][key]= value 
            #update the minfreq
            if self.minFreq == oldFreq and len(self.freqKeyMap[ oldFreq])==0:
                self.minFreq =newFreq
        else:
            #capacity reached
            if self.capacity == len(self.keyFreqMap):
                
                #evict the lfu then lru
                keytoDelete,valtoDelete = self.freqKeyMap[self.minFreq].popitem(last=False)
                self.keyFreqMap.pop(keytoDelete)
                self.freqKeyMap[1][key]=value
                self.keyFreqMap[key]=1
                self.minFreq  = 1 
    
            #capacity not reached
            self.freqKeyMap[1][key]=value
            self.keyFreqMap[key]=1
            self.minFreq  = 1 
            