"""
Objective : Insert at end in singly linked list.
Approach :-
1. If linked list is empty, insert at the first position else go to step 2.
2. Find the last node.
3. Point the next addrees pointer of the last node to the new node.
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


class InsertAtEnd:
    """
    A class representing a linked list with operations to insert nodes at the front or at the end.

    Attributes:
    - head: The reference to the first node in the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the InsertAtEnd class with an empty linked list.
        """
        self.head = None

    def insertatfront(self, value):
        """
        Inserts a new node with the given value at the front of the linked list.

        Parameters:
        - value: The value to be inserted into the new node.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data):
        """
        Inserts a new node with the specified data at the end of the linked list.

        Parameters:
        - data: The value to be inserted into the new node.
        """
        if self.head is None:
            self.insertatfront(data)
            return

        new_node = Node(data)
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def traverse(self):
        """
        Traverses the linked list, printing the value of each node.
        """
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next
        print()


# Example Usage:
obj = InsertAtEnd()
obj.insert(5)
obj.traverse()
obj.insert(100)
obj.traverse()
obj.insert(110)
obj.traverse()
obj.insert(700)
obj.traverse()
obj.insert(61)
obj.traverse()
obj.insert(26)
obj.traverse()
obj.insert(500)
obj.traverse()

"""
Ouput :-
  5->
  5->100->
  5->100->110->
  5->100->110->700->
  5->100->110->700->61->
  5->100->110->700->61->26->
  5->100->110->700->61->26->500->
"""
