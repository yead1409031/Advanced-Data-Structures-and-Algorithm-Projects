import sys

DEBUG = False

class Heap:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = [None]
        
    def getData(self):
        return self.data[:self.size]
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0

    def __siftUp(self, child):
        parent = (child - 1) // 2
        while (child > 0) and (self.data[child] > self.data[parent]):
            temp = self.data[child]
            self.data[child] = self.data[parent]
            self.data[parent] = temp
            if DEBUG:
                print(f"{self.data[parent]} swapped with {self.data[child]}")
            child = parent
            parent = (child - 1) // 2

    def buildFrom(self, seq):
        self.data = [None]*len(seq)
        self.size = self.capacity = len(seq)

        for x in range(self.size):
            self.data[x] = seq[x]
            
        index = (2 * self.data.index(seq[0])) + 1

        while (index < len(seq)):
            self.__siftUp(index)
            index += 1

    def addToHeap(self, newVal):
        if (self.size == self.capacity):
            self.capacity *= 2
            temp = [None] * self.capacity
            
            for i in range(self.size):
                temp[i] = self.data[i]
                
            self.data = temp

        self.data[self.size] = newVal
        self.__siftUp(self.size)
        self.size += 1
        
        return newVal

    def __largestChild(self, index, lastIndex):
        ''' Inputs:
            - index -> index of the current node
            - lastIndex -> index of the last node in the heap
            Output:
            - index of the largest child if it exists, None otherwise
        '''
        # find indexes of left and right child of the current (index) node
        # return None if left child index is past last index
        # otherwise return the index of the largest child

        left=2*index+1 #find index of the left child
        right=2*index+2 #find index of the right child
       
        if left>lastIndex: #check whether left child index is past last index
            return None # return none because there is no left child
        elif right>lastIndex: #check whether right child index is greater than last index 
            return left #return left child because there is no right child
                
        else: # that means there are two childs exist
            if self.data[right]>self.data[left]: #check whether right child data is bigger than that of left
                return right #return right as it's bigger than the other
            else: # means right child data is less than or equal to left child data
                return left #return left because left child data is equal or greater than right child data

        
    def __siftDownFromTo(self, fromIndex, last):
        ''' Inputs:
            - fromIndex -> index of the node where to start sifting from
            - last -> index of the last node in the heap
            Output:
            - the node sifted down as far as necessary to maintain heap conditions
        '''
        
        # repeat until node is in the right position
        #   find index of a largest child
        #   if index of the largest child is not found then finish
        #   otherwise, if value of the largest child is larger than parent then swap       
        

        current=fromIndex # it's actually the index of root node or 0th position #index of the node to start sifting from 
        child=self.__largestChild(current,last) #determine the index of the largest child of current node
        
        # repeat until node is in the right position
        while child is not None and self.data[current]<self.data[child]: # check whether there is child and whether if current noda data is less than its child data
            self.data[current],self.data[child]=self.data[child],self.data[current] #swap greater child with current node 
            current=child # now swapped child is current node for iteration
            child=self.__largestChild(current,last) #Again, determine the index of the largest child of new current node for while comparison and iteration
        


    def sort(seq):
        
        h = Heap()
        h.buildFrom(seq)
        
        for i in range(len(seq)):
            h.data[0], h.data[h.size - 1] = h.data[h.size - 1], h.data[0]
            h.size -= 1
            h.__siftDownFromTo(0, h.size - 1)
        return h.data
        
    def __str__(self):
        st = f"\tHeap size: {(self.size)}.\n"
        st += f"\tHeap capacity: {(self.capacity)}.\n"
        st += f"\tElements of heap: \n"
        for x in range(self.size):
            st += f"\t\tValue: {(self.data[x])} at index: {x}\n"
        return st 
    def __repr__(self):
        return self.__str__()

def main():

    file = open(sys.argv[1], "r")
    for line in file:
        values = [int(x) for x in line.split()]
        
    print(f"Original list: {values}\n")

    h=Heap() #Assign Heap class into h variable
    h.buildFrom(values) #build heap according to the input values

    print(f"Heapified list:\n{h}")
    
    sorted_list = Heap.sort(values)
    print(f"Sorted list: {sorted_list}")

main()

    
#reference:
#https://stackoverflow.com/questions/56724342/why-is-siftdown-working-in-heapsort-but-not-siftup
#https://www.programiz.com/dsa/heap-sort
#https://www.geeksforgeeks.org/heap-data-structure/