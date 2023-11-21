"""
Objective : Insertion at the front of the linked list.

Approch : 
1. Create a new node with the given data and next adderess as Null.
2. Point next address pointer to head.
3. Assign head to the newly created node.
"""


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
    - data: The value stored in the node.
    - next: A reference to the next node in the linked list.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Node class.

        Parameters:
        - value: The value to be stored in the node.
        """
        self.data = value
        self.next = None


class InsertAtFront:
    """
    A class representing a linked list with an operation to insert a new node at the front.

    Attributes:
    - head: The reference to the first node in the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the InsertAtFront class with an empty linked list.
        """
        self.head = None

    def insert(self, value):
        """
        Inserts a new node with the given value at the front of the linked list.

        Parameters:
        - value: The value to be inserted into the new node.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(f"{value} got inserted.")

    def traverse(self):
        """
        Traverses the linked list, printing the value of each node.
        """
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next

        
obj = InsertAtFront()
obj.insert(5)
obj.insert(10)
obj.insert(15)
obj.traverse()

"""
Ouput :-
	5 got inserted.
	10 got inserted.
	15 got inserted.
	15->10->5->
"""
