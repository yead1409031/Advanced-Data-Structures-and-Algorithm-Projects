import sys   # Import the 'sys' module

class Trie:   # Define a class named 'Trie'
    def __init__(self):   # Define the constructor of the class, which initializes the 'start' attribute to None
        self.start = None

    class TrieNode:   # Define an inner class named 'TrieNode' inside the 'Trie' class
        def __init__(self, item, next=None, follows=None):   # Define the constructor of the inner class, which initializes the 'item', 'next', and 'follows' attributes
            self.item = item
            self.next = next
            self.follows = follows

    def __insert(node, key):   # Define a private method named '__insert' that takes two arguments, 'node' and 'key'
        if len(key) == 0:   # If the length of 'key' is 0, return None
            return None

        if node == None:   # If 'node' is None, create a new 'TrieNode' object with the first character of 'key' as the 'item' attribute, and recursively call '__insert' with None as the 'node' argument and the remaining characters of 'key' as the 'key' argument
            return Trie.TrieNode(key[0], None, Trie.__insert(None, key[1:]))

        if key[0] == node.item[0]:   # If the first character of 'key' is the same as the first character of the 'item' attribute of 'node', recursively call '__insert' with 'node.follows' as the 'node' argument and the remaining characters of 'key' as the 'key' argument
            node.follows = Trie.__insert(node.follows, key[1:])
            return node

        node.next = Trie.__insert(node.next, key)   # Otherwise, recursively call '__insert' with 'node.next' as the 'node' argument and 'key' as the 'key' argument, and set the 'next' attribute of 'node' to the result of the recursive call
        return node   # Return 'node'

    def insert(self, key):   # Define a method named 'insert' that takes one argument, 'key'
        self.start = Trie.__insert(self.start, key + "$")   # Call '__insert' with 'self.start' as the 'node' argument and 'key + "$"' as the 'key' argument, and set the 'start' attribute of the instance to the result of the recursive call

    def __contains(node, key):   # Define a private method named '__contains' that takes two arguments, 'node' and 'key'
        if len(key) == 0:   # If the length of 'key' is 0, return True
            return True
        if node == None:   # If 'node' is None, return False
            return False
        if key[0] == node.item[0]:   # If the first character of 'key' is the same as the first character of the 'item' attribute of 'node', recursively call '__contains' with 'node.follows' as the 'node' argument and the remaining characters of 'key' as the 'key' argument
            return Trie.__contains(node.follows, key[1:])
        return Trie.__contains(node.next, key)   # Otherwise, recursively call '__contains' with 'node.next' as the 'node' argument and 'key' as the 'key' argument

    def __contains__(self, key):
    # This is a special method that allows objects of the Trie class to be checked for membership using the `in` operator
        return Trie.__contains(self.start, key + "$")

    def __str(node, indent):
        if node == None:
            return ""
        # This method is called when the Trie object is converted to a string using the str() function
        # It returns a string representation of the Trie object
        return f"\n{indent}{str(node.item)}{Trie.__str(node.follows, indent + ' ')}{Trie.__str(node.next, indent)}"

    def __str__(self):
        # This is another special method that returns a string representation of the Trie object
        # It calls the __str() method and passes the start node and an empty string as arguments
        return Trie.__str(self.start, "")
    
    def main():
        # This function is the main entry point of the program
        words_file = "dict.txt"
        input_file = "test.txt"
        # Build trie from words file
        trie = Trie()
        with open(words_file, 'r') as f:
            for line in f:
                # Read each line from the words file
                word = line.strip()
                # Insert the word into the trie
                trie.insert(word)

        # Spell-check input file
        with open(input_file, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                # Read each line from the input file
                words = line.split()
                for word_num, word in enumerate(words, start=1):
                    # Remove leading/trailing punctuation and convert to lowercase
                    word = word.lower().strip(',').strip('.')
                    # Check if the word is in the trie
                    if word not in trie:
                        # Print the misspelled word
                        print("Misspelled words: ", word)
if __name__ == '__main__':
    main() 



