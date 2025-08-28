import random

# Node class for singly linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Singly linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    # Method to print the list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    # Method to sort the list using selection sort algorithm
    def selection_sort(self):
        current_node = self.head
        while current_node:
            min_node = current_node
            next_node = current_node.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            current_node.data, min_node.data = min_node.data, current_node.data
            current_node = current_node.next

# User input for number of nodes
n = int(input("Enter number of nodes: "))

# Create linked list with random values in range 0 to 100
linked_list = LinkedList()
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
