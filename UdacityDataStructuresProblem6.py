''' **********************************************************
Importing Libraries
***********************************************************'''
import random
import numpy as np

''' **********************************************************
Defining Classes
***********************************************************'''

class Node:

    '''

    Class to generate nodes that can be used as base to
    generate linkedlists

    '''
    
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    '''

    Class to generate linkedlist, which can be used to
    implement operations such as unions and intersections.
    Moreover, it contains methods that can facilitate the
    processing of the linkedlists content, as the removing
    of duplicated elements and sorting methods.

    '''
    
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

    def copy_list(self):

        new_list = LinkedList()

        node = self.head
        while node.next is not None:
            new_list.append(node.value)
            node = node.next
        new_list.append(node.value)            

        return new_list

    def remove_duplicates(self):

        try:
            node2compare = self.head
            while (node2compare.next is not None) and (node2compare.next.next is not None):
                node2search = node2compare
                while node2search.next is not None:
                    if node2compare.value == node2search.next.value:
                        node2search.next = node2search.next.next
                    else:
                        node2search = node2search.next
                node2compare = node2compare.next

            if node2compare is not None:
                
                if node2search.value == node2compare.value:
                    node2compare.next = None
        except:
            print('\nError: Lists contain not valid elements for this operation, need to be integers.\n')

        
    def bubbleSort(self):
        swapped = True
     
        while swapped:
            swapped = False
            current = self.head
     
            while current.next:
                if current.value > current.next.value:
                    tmp = current.next.value
                    current.next.value = current.value
                    current.value = tmp
                    swapped = True
                current = current.next


''' **********************************************************
Defining Functions
***********************************************************'''

def union(llist_1, llist_2):

    '''

    Functio to find the union of elements between two linkedlists

    Inputs:

    llist_1 -> Linkedlist containing elements to find the union
    llist_2 -> Linkedlist containing elements to find the union

    Output:

    union -> Union of elements between llist_1 and llist_2

    '''    

    if (llist_1.head == None):
        union = llist_2.copy_list()
        union.remove_duplicates()
        union.bubbleSort()
        return union
    if (llist_2.head == None):
        union = llist_1.copy_list()
        union.remove_duplicates()
        union.bubbleSort()
        return union

    union = llist_2.copy_list()
    
    node = llist_1.head
    while node.next is not None:
        union.append(node.value)
        node = node.next
    union.append(node.value)

    if union.head is not None:
        union.remove_duplicates()
        union.bubbleSort()
    
    return union

def intersection(llist_1, llist_2):

    '''

    Function to find the intersection of elements between two
    linkedlists

    Inputs:

    llist_1 -> Linkedlist containing elements to find the intersection
    llist_2 -> Linkedlist containing elements to find the intersection

    Output:

    intersection -> intersection of elements between llist_1 and llist_2

    '''

    if (llist_1.head == None):
        intersection = llist_2.copy_list()
        intersection.remove_duplicates()
        intersection.bubbleSort()
        return union
    if (llist_2.head == None):
        intersection = llist_1.copy_list()
        intersection.remove_duplicates()
        intersection.bubbleSort()
        return union

    intersection = LinkedList()

    node2compare = llist_1.head
    while node2compare.next is not None:
        node2search = llist_2.head
        while node2search.next is not None:
            if node2compare.value == node2search.value:
                intersection.append(node2compare.value)
                break
            node2search = node2search.next
        node2compare = node2compare.next
    if node2compare.value == node2search.value:
        intersection.append(node2compare.value)

    if intersection.head is not None:
        intersection.remove_duplicates()
        intersection.bubbleSort()
    
    return intersection

''' **********************************************************
Running Code - Main
***********************************************************'''

if __name__ == "__main__":

    print('\n------------------- UDACITY CASE 1 -------------------\n')

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print('LinkedList 1: \n', linked_list_1.__str__())
    print('LinkedList 2: \n', linked_list_2.__str__())
    print()
    print ('Union Result: \n', union(linked_list_1,linked_list_2))
    print ('Intersection Result: \n', intersection(linked_list_1,linked_list_2))
    print()

    print('\n------------------- UDACITY CASE 2 -------------------\n')

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print('LinkedList 3: \n', linked_list_3.__str__())
    print('LinkedList 4: \n', linked_list_4.__str__())
    print()
    print ('Union Result: \n', union(linked_list_3,linked_list_4))
    print ('Intersection Result: \n', intersection(linked_list_3,linked_list_4))

    ######################## CUSTOM CASES ###############################
    
    Case1 = ([1,2,3,4,5,6,7,8,9,10], [2,4,6,8,10])
    Case2 = ([1,np.nan,np.nan,int(2e10),int(3e20)], [int(1e10),2,np.nan,int(3e20)])
    Case3 = ([random.randint(0, 50) for n in range(20)], [random.randint(0, 50) for n in range(20)])
    Cases = [Case1, Case2, Case3]
    
    for k, case in enumerate(Cases):

        linked_list_A = LinkedList()
        linked_list_B = LinkedList()

        element_A = case[0]
        element_B = case[1]

        for i in element_A:
            linked_list_A.append(i)

        for i in element_B:
            linked_list_B.append(i)        

        print('\n--------------------- TEST CASE {}  ---------------------\n'.format(k+1))
        print('LinkedList A: \n', linked_list_A.__str__())
        print('LinkedList B: \n', linked_list_B.__str__())
        print()
        print ('Union Result: \n', union(linked_list_A,linked_list_B))
        print ('Intersection Result: \n', intersection(linked_list_A,linked_list_B))

''' **********************************************************
END
***********************************************************'''
