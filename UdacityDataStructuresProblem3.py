''' **********************************************************
Importing Libraries
***********************************************************'''
import sys

''' **********************************************************
Defining Classes
***********************************************************'''

# Use this class as the nodes in your linked list
class Node:

    '''
    Class that generate nodes that can be used in different
    data structures such as linkedins, stacks, trees, among others.

    The class objects are composed by a node index and value, childs
    bits and flags.
    '''
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.bit = None
        self.next = None
        self.flag = 0

    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"        


# Use this class as the nodes in your linked list
class Queue:

    '''
    Class that can be used to generate queues, which
    can be used when bulding a Huffman Encoder as
    required.
    
    '''
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, NodeTree):
        new_node = NodeTree
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    def dequeue(self):
        if self.is_empty():
            return None

        node = self.head
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return node

    def enqueue_head(self, NodeTree):

        new_node = NodeTree
        flag = 0
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        elif new_node.value == self.tail.value:
            node =  self.head
            while node.next is not None:
                node_prev = node
                node = node.next

            node_tmp = self.tail
            self.tail = node_prev
            self.enqueue(new_node)
            self.enqueue(node_tmp)

            return

        elif new_node.value > self.tail.value:
            self.enqueue(new_node)
            return

        node = self.head
        while node is not None:
         
            if new_node.value <= node.value:
                if node == self.head:
                    new_node.next = self.head
                    self.head = new_node
                    self.num_elements += 1 
                    break                  
                else:
                    new_node.next = node
                    node_prev.next = new_node
                    self.num_elements += 1 
                    break
            node_prev = node                
            node = node.next
   
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

''' **********************************************************
Defining Functions
***********************************************************'''

# Use this class as the nodes in your linked list
def Exploring_Tree(Tree):

    '''
    Function used to explore or set specific values within
    a tree nodes, exploring all of them.

    Inputs:

    Tree -> Tree to be explored
    '''  

    Tree.flag = 0
    
    if (Tree.left):
        Tree.left.flag = 0
        Tree.left = Exploring_Tree(Tree.left)
    if (Tree.right):
        Tree.right.flag = 0
        Tree.right = Exploring_Tree(Tree.right)

    return Tree
       

# Use this class as the nodes in your linked list
def huffman_encoding(data):

    '''
    Function used to implement a Huffman Encoder, using
    Tree based on the Node and the Queue classes.

    Inputs:

    data -> Data to be encoded using the Huffman encoder

    Output:

    Tree -> Tree used to encode the data
    Path -> Path containing the binary encoded data as a list
    
    '''

    # Creating the encoding basic table:
    data = data.upper()
    count_table = {}
    data_queue = Queue()
    
    for char in data:
        if char not in count_table.keys():
            count_table[char] = data.count(char)
        data_queue.enqueue(Node(None, char))


    # Creating list containing the countin table
    Encoding = Queue()
    count_table = dict(sorted(count_table.items(), key=lambda item: item[1], reverse=False))
    for key in count_table.keys():
        Encoding.enqueue(Node(key, count_table[key]))

    node = Encoding.head
    Tree = Node(None, None)
    counter = 1
    
            
    while node.next is not None:
        
        Node1 = Encoding.dequeue()
        Node2 = Encoding.dequeue()


        if Tree.key == None:
            Tree_tmp = Node('Internal '+str(counter), Node1.value+Node2.value)
            counter += 1
            Tree = Tree_tmp
            Tree.left = Node1
            Tree.right = Node2
        else:
            Tree = Node('Internal '+str(counter), Node1.value+Node2.value)
            counter += 1
            Tree.left = Node1
            Tree.right = Node2

        
        Tree.left.bit = 0
        Tree.right.bit = 1    
        Encoding.enqueue_head(Tree)
        node = Encoding.head

    path = ''
    node = data_queue.dequeue()
    Path = []

    while node is not None:
        node_tree = Tree        
        Tree_root = Tree
        flag = 0
        tmp_path = ''
        local_path = '' 

        while(True):    


            if node_tree.key.split()[-1] != str(0):

                condition1 =('Internal' in node_tree.left.key) and ('Internal' in node_tree.right.key)
                condition2 = ('Internal' in node_tree.left.key) and ('Internal' not in node_tree.right.key)
                condition3 = ('Internal' not in node_tree.left.key) and ('Internal' in node_tree.right.key)

                if condition1:
                    if (node_tree.left.flag != flag) and (node_tree.right.flag != flag):
                        node_tree.flag = 1 
                        node_tree = Tree_root
                        local_path = tmp_path                    
                    elif (node_tree.left.flag == flag) and((int(node_tree.left.key.split()[-1])) < (int(node_tree.right.key.split()[-1]))):                  
                        node_tree = node_tree.left
                        local_path += '0'
                    elif (node_tree.right.flag == flag) and ((int(node_tree.left.key.split()[-1])) > (int(node_tree.right.key.split()[-1]))):
                        local_path += '1'
                        node_tree = node_tree.right                       
                    elif (node_tree.left.flag != flag) and (node_tree.right.flag == flag):                    
                        node_tree = node_tree.right
                        local_path += '1'                        
                    elif (node_tree.right.flag != flag) and (node_tree.left.flag == flag):
                        local_path += '0'
                        node_tree = node_tree.left

                elif condition2:
                    if node_tree.right.key == node.value:
                        local_path += '1'
                        break
                    elif (node_tree.left.flag == flag):
                        node_tree = node_tree.left
                        local_path += '0'
                    elif (node_tree.left.flag != flag):
                        node_tree.flag = 1
                        node_tree = Tree_root
                        local_path = tmp_path                       
                
                elif condition3:
                    if node_tree.left.key == node.value:
                        local_path += '0'
                        break
                    elif (node_tree.right.flag == flag):                       
                        node_tree = node_tree.right
                        local_path += '1'                          
                    elif (node_tree.right.flag != flag):
                        node_tree.flag = 1 
                        node_tree = Tree_root
                        local_path = tmp_path    
        
                else:
                    if node_tree.left.key == node.value:
                        local_path += '0'
                        break
                    if node_tree.right.key == node.value:
                        local_path += '1'
                        break
                    else:
                        local_path = tmp_path
                        node_tree = Tree_root


            if ('Internal' not in node_tree.left.key) and ('Internal' not in node_tree.right.key):
                node_tree.flag = 1

            if str(0) == node_tree.key.split()[-1]:
                if node_tree.left.key == node.value:
                    local_path += '0'
                    break
                if node_tree.right.key == node.value:
                    local_path += '1'
                    break
                else:
                    Tree_root = Tree.right
                    node_tree = Tree.right
                    tmp_path = '1'
                    local_path = tmp_path
                    node_search_value = 0


        Path.append(local_path)
        Exploring_Tree(Tree)
        node = data_queue.dequeue()
                        
    return Tree, Path


# Use this class as the nodes in your linked list
def huffman_decoding(data,tree):

    '''
    Function used to decoded encoded data using a
    Huffman tree represented by the tree input. 

    Inputs:

    data -> Encoded data
    tree -> Tree used to encoded the data, the Huffman encoder

    Output:

    path -> Decoded data using the Huffman Encoder Tree
    
    '''  

    count_table = {}

    data_queue = Queue()

    for char in data:
        if char not in count_table.keys():
            count_table[char] = data.count(char)
        data_queue.enqueue(Node(None, char))

    node = data_queue.dequeue()
    node_tree = tree
    path = ''
    
    while node is not None:


        if node.value == '0':
            node_tree = node_tree.left
        else:
            node_tree = node_tree.right


        if 'Internal' not in node_tree.key:
            path += node_tree.key
            node_tree = tree

        node = data_queue.dequeue()

    return path

''' **********************************************************
Running Code - Main
***********************************************************'''

if __name__ == "__main__":

    print('\n-------------------- UDACITY CASE --------------------\n')
          
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    tree, encoded_data = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(''.join(encoded_data), base=2))))
    print ("The content of the encoded data is: {}\n".format(''.join(encoded_data)))

    decoded_data = huffman_decoding(''.join(encoded_data), tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    Case1 = 'Samus Aran'
    Case2 = 'You must be the change you wish to see in the world!'
    Case3 = '''The discipline of strength instills resistance without complaint,
    and also teaches courtesy. It demands that we not ruin the pleasure or
    serenity of others through the expression of our own sadness or pain.'''
    Cases = [Case1.upper(), Case2.upper(), Case3.upper()]

    for i, case in enumerate(Cases):

        print('--------------------- TEST CASE {}  ---------------------\n'.format(i+1))
        Tree, path = huffman_encoding(case)
        print('Data to Encode:\n',case,'\n')
        print('Encoded_data:\n', ''.join(path), '\n')
        dec_case = huffman_decoding(''.join(path),Tree)
        print('Decoded data:\n', dec_case, '\n')

''' **********************************************************
END
***********************************************************'''
