DEBUG=True
class Heap:
    def __init__(self):
        self.size=0
        self.capacity=1
        self.data=[None]
    
    def getData(self):
        return self.data[:self.size]
    def getSize(self):
        return self.sizedef 
    def isEmpty(self):
        return self.size==0
    
    def __siftUp(self,child): #child=undex
        parent=(child-1)//2

        while (child>0) and (self.data[child]>self.data[parent]):
            temp=self.data[child]
            self.data[child]=self.data[parent]
            self.data[parent]=temp

            if DEBUG:
                print(f"{self.data[parent]} swapped with {self.data[child]}")
                child=parent
                parent=(child-1)//2

               


    
    def buildForm(self,seq):
        self.data=[None]*len(seq)
        
        self.size=self.capacity=len(seq)

        for x in range(self.size):
            self.data[x]=seq[x]

        index=(2*self.data.index(seq[0]))+1

        while (index<len(seq)):
            self.__siftUp(index)
            index+=1
    
    def addToHeap(self,newVal):
        if (self.size==self.capacity):
            self.capacity*=2
            temp=[None]*self.capacity
            for i in range(self.size):
                temp[i]=self.data[i]
            self.data=temp
        self.data[self.size]=newVal
        self.__siftUp(self.size)
        self.size+=1
        return newVal
    
    def __largestChild(self,Index,lastIndex)
        
        pass
    
    def __siftDownFromTo(self,fromIndex,last):
        #__largestChild(parent,last)

        pass
    
    def sort(seq):
        h=Heap()
        h.buildForm(seq)
        for i in range(len(seq)):
            h.data[0],h.data[h.size-1]=h.data[h.size-1],h.data[0]
            h.size -=1
            h.__siftDownFromTo(0,h.size-1)
            return h.data

    

    def __str__(self):
        st=f"\tHeap size: {(self.size)}\n"
        st += f"\tHeap capacity: {(self.capacity)}.\n"
        st+=f"\tElements of heap: \n"
        for x in range (self.size):
            st+=f"\t\tValue: {(self.data[x])} atvindex: {x}\n"
        
        def __repr__(self):
            return self.__str__()
        
    def main():
        h=Heap()
        print(f"Heap is empty: {h.isEmpty()}")
        print(f"Heap size: {h.getSize()}")
        print(f"Heap data: {h.getData()}")
        print()
        #h.buildForm([71,5,36])
        print()
        print(f"Heap is empty: {h.isEmpty()}")
        print(f"Heap size: {h.getSize()}")
        print(f"Heap data: {h.getData()}")
        h.addToHeap(57)
        h.addToHeap(101)
        h.addToHeap(103)
        print("Heap: ")
        print(h)

    main()