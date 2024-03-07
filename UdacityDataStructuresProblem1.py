''' **********************************************************
Importing Libraries
***********************************************************'''
import os
os.system ("cls")
import string
import random

''' **********************************************************
Defining Classes
***********************************************************'''

# Use this class as the nodes in your linked list

class Node:
    
    '''
    Class that generate nodes that can be used in different
    data structures such as linkedins, stacks, trees, among others.

    The class objects are composed by a node index and value.
    '''

    def __init__(self, key, value):
        # Initializing class variables
        self.key = key
        self.value = value
        self.next = None
        

class LRU_Cache(object):

    '''
    Class used to define the characteristics of lined list
    objects. This are composed by Nodes which are linked
    due to the class properties, such as the head of the list
    and the next linked node.

    The class objects are defined by the capacity of the list,
    or the maximun number of nodes that can compose them.

    Moreover, the class also provide methods to display the
    list elements and order, as methods to set new nodes or
    to retrieve specific nodes informations if found
    within the created linked list.
    '''    

    def __init__(self, capacity):
        # Initializing class variables
        self.capacity = capacity
        self.head = None

    def __repr__(self):
        # Method to display the list elements and their order
        list_content = []
        node = self.head

        # Looping wihtin the list elements
        while node.next is not None:
            list_content.append((node.key, node.value))
            node = node.next

        #Displaying elements
        list_content.append((node.key, node.value))
        print(list_content)
        
                
    def get(self, key):
        # Method to get information about nodes contaned within the list

        #Defining local variables
        value2return = 'NonValue'
        prev_node = None
        
        # If list is empty return -1
        if self.head == None:
            return -1

        # Finding items locations, if present.
        node = self.head
        while node.next is not None:
            if node.key == key:
                value2return = node.value               
                if node == self.head:
                    self.head =  self.head.next
                else:
                    prev_node = tmp_node
                    next_node = node
            tmp_node = node
            node = node.next

        # Returning -1 if the element is not present
        if value2return == 'NonValue':          
            return -1
        else:
            # Returning the found value
            if prev_node is not None:
                # Re-ordering list elements following the cache
                # expected behaviour
                prev_node.next = next_node.next
            node.next  = Node(key, value2return)
            return value2return
            

    def set(self, key, value):
        # Method to insert new elements to the list
        
        # Insert the new element in the list head if the  list is empty
        if self.head == None:
            self.head = Node(key, value)
            return

        # Finding the location to add the new element, if capacity is
        # still available
        node = self.head
        count_items = 1
        while (node.next is not None) and (count_items<=self.capacity):
            node = node.next
            count_items += 1

        # If capacity if already full, removing the least accesed item to
        # allocate enough space to add the new element
        if count_items == self.capacity:
            self.head = self.head.next
        node.next = Node(key, value)

        
''' **********************************************************
Defining Functions
***********************************************************'''

def Test_Cases(case):

    if case == 1:

        print(''' ---------------- TEST CASE 1 ---------------- \n''')

        print('Starting cache with 4 slots size, with the following elements:')
        print('''(1, 1), (None, 2), (3, None), (4,4) \n''')
        our_cache = LRU_Cache(4)
        our_cache.set(1, 1);
        our_cache.set(None, 2);
        our_cache.set(3, None);
        our_cache.set(4, 4);    
        print('Cache Status: ')
        our_cache.__repr__()

        print('\nGetting value for for key 1 from the cache, result: ', our_cache.get(1))
        print('Getting value for key None from the cache, result: ', our_cache.get(None))
        print('Getting value for key 3 from the cache, result: ', our_cache.get(3))
        print('\nReviewing the cache status after getting the previous values:')        
        our_cache.__repr__()

        print('\nAdding the following elements to the cache:')
        print('''(8, 4), (7, None) \n''')
        our_cache.set(8, 4);
        our_cache.set(7, None);
        print('Cache Status: ')
        our_cache.__repr__()        
        

    if case == 2:

        print('''\n ---------------- TEST CASE 2 ---------------- \n''')

        print('Starting cache with 8 slots size, with the following elements:')
        print('''(10e18, 35e28), (20e25, 25e30), (30e24, 18e32), (40e30, 88e40) \n''')
        our_cache = LRU_Cache(8)
        our_cache.set(10e18, 35e28);
        our_cache.set(20e25, 25e30);
        our_cache.set(30e24, 18e32);
        our_cache.set(10e20, 88e30);
        print('Cache Status: ')
        our_cache.__repr__()

    
        print('\nGetting value for key 30e24 from the cache, result: ', our_cache.get(30e24))
        print('Getting value for key 8 value from the cache, result: ', our_cache.get(8))
        print('Getting value for key 10e18 from the cache, result: ', our_cache.get(10e18))
        print('\nReviewing the cache status after getting the previous values:')        
        our_cache.__repr__()


        print('''\nAdding more elements to the chache:''')
        print('''(50e38, 19e17), (80e23, 55e64), (44e14, 78e22), (25e30, 21e24) \n''')
        our_cache.set(50e38, 19e17);
        our_cache.set(80e23, 55e64);
        our_cache.set(44e24, 78e22);
        our_cache.set(25e30, 21e24);
        print('Cache Status: ')
        our_cache.__repr__()


    if case == 3:

        def id_generator(size=1, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))


        print('''\n ---------------- TEST CASE 3 ---------------- \n''')

        print('Starting cache with 8 slots size')
        our_cache = LRU_Cache(8)
        list_items = []
        for n in range(9):
            list_items.append((id_generator(), random.randint(1, 40)))

        items2add = []
        for item in random.sample(list_items,5):
            items2add.append('''({},{})'''.format(item[0],item[1]))
            our_cache.set(item[0], item[1])
        print('\nAdding Elements: \n', ','.join(items2add))
        print('\nCache Status: ')
        our_cache.__repr__()
            
        print('\nLooking for specific elements within the cache:')
        for item in random.sample(list_items,4):
            print('Getting value for key {} from the cache, result: '.format(item[0]), our_cache.get(item[0]))
        print('\nCache Status: ')
        our_cache.__repr__()

        items2add = []
        for n in range(5):
            list_items.append((id_generator(), random.randint(1, 40)))
            items2add.append('''({},{})'''.format(list_items[-1][0],list_items[-1][1]))
            our_cache.set(list_items[-1][0], list_items[-1][1])
        
        print('\nAdding Elements: \n', ','.join(items2add))
        print('\nCache Status: ')
        our_cache.__repr__()       


def main():

    print('''\n ---------------- UDACITY TEST ---------------- \n''')

    our_cache = LRU_Cache(5)   
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print('Reviewing the cache status after starting using it:')
    our_cache.__repr__()
    print()

    print('Getting key 1 value from the cache, result: ', our_cache.get(1))
    print('Getting key 2 value from the cache, result: ', our_cache.get(2))
    print('Getting key 9 value from the cache, result: ', our_cache.get(9))
    print('Reviewing the cache status after getting the previous values:')
    our_cache.__repr__()
    print()


    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print('Reviewing the cache status after adding more keys 5 and 6 values:')
    our_cache.__repr__()
    print()

    
    print('Getting key 3 value from the cache, result: ', our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print('Reviewing the cache status after getting the previous value:')
    our_cache.__repr__()
    print()

    print('''\n ---------------- CUSTOM TESTS ---------------- \n''')

    Test_Cases(case=1)

    Test_Cases(case=2)

    Test_Cases(case=3)    

''' **********************************************************
Running Code - Main
***********************************************************'''

if __name__ == "__main__":
    main()

''' **********************************************************
END
***********************************************************'''
