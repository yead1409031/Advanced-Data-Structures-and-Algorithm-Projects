from hashSet import *

class HashMap:
    class __KVPair():
        def __init__(self,key,value):
            self.key= key
            self.value=value
        #=

        def __eq__(self,other):
            if type(self)!= type(other):
                return False
            return self.key==other.key
        def getKey(self):
            return self.key
        def getValue(self):
            return self.value 
        def __hash__(self):
            return hash(self.key)
    
    def __init__(self):
        self.hSet= HashSet()
    # len(HashMap())
    def __len__(self):
        return len(self.hSet)         