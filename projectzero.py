import random

# node class creation
class Node:
    def __init__(self, data= None):
        self.data= data
        self.ref= None

# Singly Linked List class creation
class Linkedlist:
    def __init__(self):
        self.head= None
        self.tail= None

# Adding node at the end
    def append(self,data):
         new_node= Node(data)
         if self.head is None:            
            self.head= new_node
         else:             
             end_node= self.head
             while end_node.ref:
                 end_node= end_node.ref
             end_node.ref= new_node
             self.tail= new_node

# Print the list
    def print_list(self):
        present_node = self.head
        while present_node:
            print(present_node.data, end=' ')
            present_node = present_node.ref
        print()
        print("Head Data: {}".format(self.head.data)) 
        print("Tail Data: {}".format(self.tail.data)) 

# Selection sort algorithm
    def selection_sort(self):
        present_node= self.head
        while present_node:
            min_node= present_node
            next_node= present_node.ref
            while next_node:
                if next_node.data<min_node.data:                                
                  min_node= next_node
                next_node= next_node.ref 
            present_node.data, min_node.data= min_node.data, present_node.data
            present_node= present_node.ref     

#node input
n = int(input("Enter number of nodes: "))

# Create linked list with random values in range 0 to 100
linked_list = Linkedlist()
for i in range(n):
    linked_list.append(random.randint(0, 100))

# Print unsorted list
print("Unsorted list:")
linked_list.print_list()

# Sort list using selection sort algorithm
linked_list.selection_sort()

# Print sorted list
print("Sorted list:")
linked_list.print_list()



    
    
     