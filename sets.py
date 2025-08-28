class HashSet:
    def __init__(self, contents=[]):
        self.items= [None] * 10 # [none, none, none,....]
        self.numItems= 0

        for item in contents:
            self.add(item)

    def __add(item, items):
        idx= hash (item) % len(items)
        loc= -1 
        while items[idx] != None: # to check if there is item 
              if items[idx]== item:
                  return False
              if (loc<0) and (type(items[idx])== HashSet.__Placeholder):
                  loc=idx
             # [dog, cat, fish, None, ....]
              idx= (idx+1)% len(items)
        if loc<0:
            loc = idx
        items[loc]= item
        return True
    def __rehash(oldList, newList):
        for x in oldList:
            if (x!=None) and (type(x) != HashSet.__Placeholder):
                HashSet.__add(x, newList)
                return newList
    def add(self,item):
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items, [None]*2*len(self.items))

class __Placeholder:
    def __init__(self):
        pass
    def __eq__(self. other):
        return False
    

def __remove(item, items):
    idx= hash(item) % len(items)
    while items[idx] != None:
        if items[idx]==item:
            nextIdx= (idx+1) % len(items)
            if items[nextIdx]== None:
                items[idx]=None
            else:
                items[idx]= HashSet.__Placeholder()
            
            return True
        idx=(idx+1) % len(items)
    return False

def remove(self.item):
    if HashSet.__remove(item, self.items):
        self.numItems -= 1
        load= max(self.numItems, 10) / len(self.items)

        if load <= 0.25:
            self.items= HashSet.__rehash(self.items, [None]*int(len(self.items)/2))
    else:
        raise KeyError("Item: {} not in HashSet".format(item))
def discard(self.item):
    if HashSet.__remove(item, self.items):
        self.numItems -= 1
        load= max(self.numItems, 10) / len(self.items)

        if load <= 0.25:
            self.items= HashSet.__rehash(self.items, [None]*int(len(self.items)/2))

#item in HashSet
def __contains__(self.item):
    idx= hash(item) % len(self.items)
    while self.items[idx] != None:
        if self.items[idx]== item:
            return True
        idx=(idx+1) % len(self.items)
    return False
#for item in HashSet
 def __iter__(self):
    for i in range(len(self.items)):
        if (self.items[i] != None) and  (type(self.items[i] != HashSet.__Placeholder)):
            yield self.items[i] 

# HashSet a={10,20,30,40,80} 
   # HashSet a={100,30,80,40,60}
   # c=A-B/C={10,20}
   # #C=B-A /c={100,60}


                
def difference_update(self,other): #A=A-b/A.difference_update(b)-> A= self, B=other
    for item in other:
        self.discard(item)

def difference(self,other): # C=A-B/C=A.difeerence_update(B)-> A=self, B=other
    result= HashSet(self)
    result.difference_updatee(other)
    return result
def issuperset(self, other):
    for item in other:
        if item not in self:
            return False
    return True

def clear(self):
    self.numItems=0
    self.items=[None]*10

def update(self,other):
    for item in other:
        self.add(item)
# len(HashSet())
def __len__(self):
    return self.numItems
    
import sys
from HashSet import HashSet

def column (matrix, colIndex):
    col=[]
    for rowIndex in range(9):
        col.append(matrix[rowIndex][colIndex])
    return col
def getSquare(matrix, rowIndex,colIndex):
    square=[]
    for i in range(rowIndex,rowIndex+3): # range(0,3)-> [0,1,2]|range(0,3)-> [0,1,2]
        for j in range(colIndex, colIndex+3): #range(0,3)-> [0,1,2]| range(3,6)-> [3,4,5]
            square.append(matrix[i][j]) # [0][0], [0][1], [0][2]|[1][0]
    return square
    

def getGroups(matrix):
    groups= []
    for i in range(9):
        groups.append(list(matrix[i]))
    for i in range (9):
        groups.append(getColumn(matrix, i))
    for i in range(0,9,3): # range(0,9,3)-> [0,3,6]
        for j in range(0,9,3):
            groups.append(getSquare(matrix,i,j))
    return groups

def rule1(group):
    pass

def rule2(group):
    pass

def cardinality(x):
    return len(x)

def reduceGroup(group):
    changed= False
    group.sort(key=cardinality)
    changed= rule2(group)
    changed= rule1(group)

    return changed


def reduceGroups(groups):
    changed= False
    for group in groups:
        if reduceGroups(group):
            changed= True
    return changed

def reduce(matrix):
    changed= True 
    groups= getGroups(matrix)

    while changed:
        changed= reduceGroups(groups)





def printMatrix(matrix):
    for i in range(9):
        for j in range(9):
            if len(matrix[i][j]) != 1:
                sys.stdout.write("x ")
            else:
                for k in matrix[i][j]:
                    sys.stdout.write(str(k) + " ")
        sys.stdout.write("\n")

def main():
    file=open("sudoku.txt", "r")
    matrix=[]
    for line in file:
        lst= line.split()
        row=[]
        for val in lst:
            if val=='x':
                s=HashSet(range(1,10))
            else:
                s=HashSet([eval(val)])
            row.append(s)
      
        matrix.append(row)
    print("solvong this puzzle")
    printMatrix(matrix)
    reduce(matrix)
    print()
    print("Solution:")
    printMatrix(matrix)

main()