import sys

class Trie: #it defines a class named 'Trie'
    def __init__(self): #it defines a constructor method of the 'Trie' class and set start variable to None
        self.start = None

    class TrieNode: #it defines a 'TrieNode' class inside the 'Trie' class
        def __init__(self, item, next = None, follows = None): #defining the constructor for the inner 'TrieNode' class and initialize with an item, next and follows 
            self.item = item
            self.next = next
            self.follows = follows

    def __insert(node, key): #defining helper insert funtion of 'Trie' class to recursively insert a key
        if len(key) == 0: #if empty key, return None 
            return None

        if node == None: #if node is None, create new node with first unit of the key and recursively insert the subsequent units into follows link
            return Trie.TrieNode(key[0], None, Trie.__insert(None, key[1:]))

        if key[0] == node.item[0]: #if first unit of key equal current node, insert rest of the key into follows link of current node
            node.follows = Trie.__insert(node.follows, key[1:])
            return node
        
        node.next = Trie.__insert(node.next, key) #otherwise, insert key into next link of current node
        return node
    
    def insert(self, key): #insert method of 'Trie' class for inserting a key
        self.start = Trie.__insert(self.start, key+"$")

    def __contains(node, key): #defining helper contain funtion to recursively check if a given key is present 
        
        if len(key)==0:
            return True
        if node==None:
            return False
        if key[0]==node.item[0]:
            return Trie.__contains(node.follows,key[1:])
        return Trie.__contains(node.next,key)
    
    def __contains__(self, key): #defining contain method to check the presence of a given key 
        return Trie.__contains(self.start, key+"$")

    def __str(node, indent): #defining helper stringer funtion to recursively traverse and return string representation of current node's item, its follows & next node
        if node == None:
            return ""

        return f"\n{indent}{str(node.item)}{Trie.__str(node.follows, indent + ' ')}{Trie.__str(node.next, indent)}"

    def __str__(self): #stringer method for string representation of the Trie object
        return Trie.__str(self.start, "")

def main():
    words = open(sys.argv[1], "r") #assign given dict.txt file into 'words' variable
    trie = Trie() #it assigns the 'Trie' structure into the variable called 'trie'
    for line in words: #iterate over each line of dict.txt file and remove whitespace
        word = line.strip()
        trie.insert(word)  #inserting data into the trie using insert function
        
    text = open(sys.argv[2], "r") #assign input file to text
    print("Misspelled words:") #print the string named "Mispelled words"
    for line in text:
        for word in line.split():
            word = word.lower().strip(',').strip('.') #covert to lowercase #remove commas or periods
            if word not in trie: #check whether trie contains the word                                                    
                print("  ", word) #prints the misspelled word because trie doesn't contain that word
                        
main()
