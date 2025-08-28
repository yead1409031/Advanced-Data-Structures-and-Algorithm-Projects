# Provide your information as the values of these variables:
myName = 'Yead, Rahman'
myTechID = '10406508'
myTechEmail = 'yra006' #only your email id omit @latech.edu
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

  for i in group: # go through all the elements of the group
      if cardinality(i) == 1: #check if there is one element
        for j in group:
          if j != i:  
            j.difference_update(i) #removing from the other sets in the group 
            changed = True
          else:
              changed = False

  return changed
  
def rule2(group):
  ### IMPLEMENT THIS FUNCTION ###

  changed = False

  h = HashSet()

  for i in range(9):  # sets for current row/column/square
    if cardinality(group[i]) > 1: #to check if cardinality of current set is more than one
      h.clear()
      h.update(group[i]) # store the current set
      x = 0
      for j in range(9):
        if group[j] != group[i]: # for other sets
          h.difference_update(group[j])
      x = cardinality(h) # check cardinality of x
      if (x == 1):
        group[i].clear()
        group[i].update(h) # assign value of h in set

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
  file = open("test-1.txt", "r")
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
