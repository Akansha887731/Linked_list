"""
Objective : A doubly linked list implementation with various operations.

class Node:
    Represents a node in a doubly linked list.

    Attributes:
    - data: The value stored in the node.
    - next: A reference to the next node in the linked list.
    - prev: A reference to the previous node in the linked list.

class operations_on_DDL:
    Represents operations on a doubly linked list.

    Attributes:
    - head: A reference to the first node in the linked list.

    Methods:
    - insert_at_beginning(data): Inserts a new node with the given data at the beginning of the linked list.
    - insert_at_end(data): Inserts a new node with the given data at the end of the linked list.
    - insert_after_given_position(position, data): Inserts a new node with the given data after the specified position.
    - delete_at_beginning(): Deletes the node at the beginning of the linked list.
    - delete_at_end(): Deletes the node at the end of the linked list.
    - delete_after_given_position(position): Deletes the node after the specified position.
    - traverse(): Traverses the linked list, printing the value of each node.
"""

class Node: 
    def __init__(self, value): 
        """
        Initializes a new instance of the Node class.

        Parameters:
        - value: The value to be stored in the node.
        """
        self.next = None  
        self.prev = None  
        self.data = value 

class operations_on_DDL:
    def __init__(self):
        """
        Initializes a new instance of the operations_on_DDL class.
        """
        self.head = None
        
    def insert_at_beginning(self, data):
        """
        Inserts a new node with the given data at the beginning of the linked list.

        Parameters:
        - data: The value to be stored in the new node.
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            return        
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    def insert_at_end(self, data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Parameters:
        - data: The value to be stored in the new node.
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            return  
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = node
        node.prev = temp_node
        
    def insert_after_given_position(self, position, data):
        """
        Inserts a new node with the given data after the specified position.

        Parameters:
        - position: The position after which the new node should be inserted.
        - data: The value to be stored in the new node.
        """
        node = Node(data)
        c = 0
        temp_node = self.head
        while c < position and temp_node.next:
            temp_node = temp_node.next
            c += 1
        node.next = temp_node.next
        temp_node.next.prev = node
        temp_node.next = node
        node.prev = temp_node
        
    def delete_at_beginning(self):
        """
        Deletes the node at the beginning of the linked list.
        """
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None 
        
    def delete_at_end(self):
        """
        Deletes the node at the end of the linked list.
        """
        node = self.head
        while node.next.next:
            node = node.next
        node.next.prev = node.next = None
        
    def delete_after_given_position(self, position):
        """
        Deletes the node after the specified position.

        Parameters:
        - position: The position after which the node should be deleted.
        """
        c = 0
        node = self.head
        while c < position and node.next:
            node = node.next
            c += 1
        temp = node.next
        temp.next.prev = node
        node.next = temp.next
        temp.next = temp.prev = None
        
    def traverse(self):
        """
        Traverses the linked list, printing the value of each node.
        """
        node = self.head
        while node:
            print(node.data, end='<=>')
            node = node.next
        print()

# Example Usage:
obj = operations_on_DDL()
obj.insert_at_beginning(8)
obj.insert_at_beginning(3)
obj.insert_at_end(39)
obj.insert_at_end(81)
obj.traverse()
obj.insert_after_given_position(2, 100)
obj.insert_after_given_position(1, 200)
obj.traverse()
obj.delete_at_beginning()
obj.traverse()
obj.delete_at_end()
obj.traverse()
obj.delete_after_given_position(1)
obj.traverse()

"""
Output :-
  3<=>8<=>39<=>81<=>
  3<=>8<=>200<=>39<=>100<=>81<=>
  8<=>200<=>39<=>100<=>81<=>
  8<=>200<=>39<=>100<=>
  8<=>200<=>100<=>
"""
