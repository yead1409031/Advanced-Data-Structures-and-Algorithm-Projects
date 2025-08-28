# Provide your information as the values of these variables:
myName = 'first_name, last_name'
myTechID = '0000000'
myTechEmail = 'abc123' #only your email id omit @latech.edu
###########################################################

import sys
from hashSet import HashSet

def getColumn(matrix, colIndex):
  col = []
  for rowIndex in range(9):
    col.append(matrix[rowIndex][colIndex])
    
  return col

def getSquare(matrix, rowIndex, colIndex):
  square = []
  for i in range(rowIndex, rowIndex+3): 
    for j in range(colIndex,colIndex+3):
        square.append(matrix[i][j])
        
  return square

def getGroups(matrix):
  groups = []
  # get rows
  for i in range(9):
    groups.append(list(matrix[i]))
  # get columns
  for i in range(9):
    groups.append(getColumn(matrix,i))
  # get squares
  # squares are processed left-right, up-down
  for i in range(0,9,3): 
    for j in range(0,9,3):
      groups.append(getSquare(matrix,i,j))     

  return groups

def cardinality(x):
  return len(x)

def rule1(group):
  ### IMPLEMENT THIS FUNCTION ###

  changed = False
  for item1 in group:
      n = cardinality(item1)
      if n == 1:
        for item3 in group:
          if not item3 == item1:
            item3.difference_update(item1)
            changed = True
          else:
              changed = False

  return changed

def rule2(group):
  ### IMPLEMENT THIS FUNCTION ###

  
  # RULE 2 - Reduce set size by throwing away elements that appear in other
  
  changed = False
  temp = HashSet()

  for i in range(9):  # 9 sets in current r/c/s
    n = cardinality(group[i]) # cardinality of current set
    if n > 1:
      temp.clear()
      temp.update(group[i]) # record the current set
      t = 0
      for j in range(9):
        if group[j] != group[i]: # if ith and jth element is not the same:
          temp.difference_update(group[j])
      t = cardinality(temp) # check cardinality of t
      if (t == 1):
        group[i].clear()
        group[i].update(temp) # assign value of temp in set

  return changed

 
def reduceGroup(group):
  changed = False 
  # this sorts the sets from smallest to largest based cardinality
  group.sort(key=cardinality)
  changed = rule2(group)
  changed = rule1(group)
  
  
  return changed

def reduceGroups(groups):
  changed = False
  for group in groups:
    if reduceGroup(group):
      changed = True
      
  return changed

def reduce(matrix):
    changed = True
    groups = getGroups(matrix)
    
    while changed:
        changed = reduceGroups(groups)

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
  file=open("test-2.txt",'r')
  matrix = []

  for line in file:
    lst = line.split()
    row = []

    for val in lst:
      if val == 'x':
        s = HashSet(range(1,10))
      else:
        s = HashSet([eval(val)])
      row.append(s)

    matrix.append(row)

  print("Solving this puzzle:")
  printMatrix(matrix)

  reduce(matrix)  

  print()
  print("Solution:")
  printMatrix(matrix)
  
main()
