"""
Objective : Insert a node at given postion in singly linked list.
Approch :-
1. If the lnked list is empty, create a node and insert the data at the beginning.
2. Check if the given postion exists in the list. If not, throw "Index out of range message".
3. If the given postion exists, then :-
	a. Point next addess pointer of the  previous node to the new node.
 	b. Point next addess pointer of the new node to the next of previous node.
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


class InsertAtPosition:
    """
    A class representing a linked list with operations to insert nodes at the front or at a specified position.

    Attributes:
    - head: The reference to the first node in the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the InsertAtPosition class with an empty linked list.
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

    def insert(self, data, position):
        """
        Inserts a new node with the specified data at the given position in the linked list.

        Parameters:
        - data: The value to be inserted into the new node.
        - position: The position in the linked list where the new node should be inserted.

        Returns:
        - If insertion is successful, returns a string indicating the success.
        - If the position is out of range, returns a string indicating an index out of range.
        """
        if self.head is None:
            self.insertatfront(data)
            return f"{data} got inserted at the beginning."

        c = 0
        prev_node = self.head
        new_node = Node(data)

        while c < position:
            prev_node = prev_node.next
            c += 1
        if prev_node is None:
            return f"{position} Position: Index out of range."

        temp_next_address = prev_node.next
        prev_node.next = new_node
        new_node.next = temp_next_address
        return f"Inserted after {position} position."

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
obj = InsertAtPosition()
obj.insert(5, 10)
obj.traverse()
obj.insert(100, 0)
obj.traverse()
obj.insert(110, 1)
obj.traverse()
obj.insert(700, 0)
obj.traverse()
obj.insert(61, 3)
obj.traverse()
obj.insert(26, 0)
obj.traverse()
obj.insert(500, 5)
obj.traverse()


"""
Ouput :-
	5->
	5->100->
	5->100->110->
	5->700->100->110->
	5->700->100->110->61->
	5->26->700->100->110->61->
	5->26->700->100->110->61->500->
"""
