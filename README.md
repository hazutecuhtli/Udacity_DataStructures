# Introduction to the Project

## Data Structure Questions

For this project, six different questions will be answered the as presented in the following content. The questions cover a variety of topics related to the data structures related to what it is covered in the ***Data Structures*** section of the ***Data Structures and Algorithms*** *Udacity* course. Questions will be answered by implementing clean and efficient *Python* code, as well as a text explanation of the most relevant characteristics of the impemented code.

# Questions 

## Problem 1: LRU Cache

Least Recently Used Cache We have briefly discussed caching as part of a practice problem while studying hash maps.The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache. In case of a cache hit, your get() operation should return the appropriate value. In case of a cache miss, your get() should return -1. While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

### Solution

The solution was possible relying on a linked list to emulate the memory cache, moving their elements depending on how they are accessed. Moreover, if the size of the created linkedlist is full, the cache size, then the least used element will be removed so it can liberate space to add a new element as required.  

For this solution a Node and a Linkedlist classes were created, for the implementation of the cache memory as a linkedlist composed by connected nodes. The implemented solution can be observed on the file named ***UdacityDataStructuresProblem1.py***.

In terms of time complexity, the get operation has a complexity of *O(n)*, while the set operation has a *O(1)* complexity. Furthermore, space complexity is limited by the cache size, which in this case has a limited of 5 elements, and therefore, it has a complexity of *O(n)*. 

## Problem 2: File Recursion

Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

### Solution

For this solution recursion and the os python module were used to achieve the expected result. Recursion is used to evaluate the different levels of the directory used as input to the functions while the os library is used to get all elements found on each of the mentioned levels. The implemented solution can be observed on the file named ***UdacityDataStructuresProblem2.py***.

In addition, in terms of time complexity, this solution has a complexity of *O(m^n)*, where n represents the number of files composing directories and m is the number of directories to look for the defined suffix. Moreover, in terms of memory space, complexity is equal to *O(m n)*.

## Problem 3: Huffman Coding

### Overview - Data Compression

In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.

### Solution

This solution consists of the implementation of a Huffman encoder and decoder, using a tree as the Huffman encoder, where the path followed to store a specific character is used for encoding or decoding characters as can be seen in the file named ***UdacityDataStructuresProblem3.py***. This solution can be divided into two stages; the building of the binary tree that represents the Huffman encoder and the decoding of data using the mentioned tree.

The encoder was built using a linkedlist composed of nodes, which are joined by subtracting, iteratively, the two smaller elements until having a single node. The results of those operations are arranged in a binary tree, which can be considered the Huffman encoder. The tree edges represent binary values that can be used to determine the path for encoding specific characters, which can also be used to decode binary encoded messages; also known as the implementation of the Huffman decoder.

The time complexity for this solution can be explained with *O(m n)* for the Huffman encoders and decoders, where m represents the letters to encode and decode, and n is the number of nodes composing the binary tree. This is because each letter to be encoded or decoded needs to be compared against most of the nodes until fulfilling the desired binary tree search. On the other hand, space complexity is of *O(n)*, since the binary tree needs to be stored in memory for the encoding and decoding operations. 

## Problem 4: Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

### Solution

This solution was implemented using the Group class to organize the group as users like in a dictionary or hash structure. The coded function is used to look for specific users within specific groups. Thus, if an active directory is represented by a specific group, it is possible to know, by using the programmed, function if a specific user is part of the active directory. More information can be seen about this solution in the file named ***UdacityDataStructuresProblem4.py***.

For this solution time complexity is defined as *O(1)*, since it is just a search over a specific group, while space complexity is defined by *O(n)*, the number of key-value pairs stored in the hash-map or dictionary. 

## Problem 5: Blockchain

A Blockchain(opens in a new tab) is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256(opens in a new tab) hash, the Greenwich Mean Time(opens in a new tab) when the block was created, and text strings as the data.

### Solution

This solution was possible by creating the block and blockchain classes, which can be seen as nodes and linkedlist, respectively. The block is used to create a linkedlist, or blockchain, where the block or node properties are defined following the blockchain structure, as presented in the introduction of this problem. More information can be seen in the shared file ***UdacityDataStructuresProblem5.py***.

In this case time complexity can be explained by *O(n)*, the number of blocks that compose the blockchain, or the number of nodes that compose a linkedlist. In addition, space complexity is also defined by *O(n)*, where n represents the number of blocks to be stored in memory.

## Problem 6: Union and Intersection

Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

### Solution

Functions created for this problem rely on two different methods added to the linkedlist class used as a base. These two methods are used to remove duplicated elements within the linkedlist used and to sort their elements for a more friendly display of the obtained results.

Then, the two create functions for this problem generate two different linkedlists composed by the union of elements between linkedlists used as inputs to the functions or to find elements present on both inputs, respectively. This is possible by searching the list as presented in the shared file ***UdacityDataStructuresProblem6.py***.

This solution generates times complexities of *O(n)* for the removing of duplicated elements within the inputs list, *O(n^2)* for the implementation of the bubble-search method, complexity of *O(n log n)* for the Union operation and a complexity of *O(n)* for the intersection operation, where n represents the number of elements considering both lists for the union and intersection operations, or the number of elements within a list for the rest of the cases.

In terms of space complexity, the union operation has a complexity of *O(n)*, while the intersection operation has a complexity of *O(m)*, where m represents the size of the smaller set. 