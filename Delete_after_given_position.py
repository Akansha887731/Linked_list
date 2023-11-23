"""
Objective: Deletion after given position of singly linked list.
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


class DeleteAtGivenPosition:
    """
    A class representing a singly linked list with an operation to delete a node after a given position.

    Attributes:
    - head: A reference to the first node in the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the DeleteAtGivenPosition class.
        """
        self.head = None

    def delete_after_given_position(self, position):
        """
        Deletes the node after the given position in the linked list.

        Parameters:
        - position: The position after which the node should be deleted.
        """
        c = 0
        node = self.head
        while c < position and node.next is not None:
            node = node.next
            c += 1
        if node.next is None:
            return
        temp = node.next
        node.next = temp.next
        temp.next = None

    def insertatfront(self, value):
        """
        Inserts a new node with the given value at the front of the linked list.

        Parameters:
        - value: The value to be stored in the new node.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Parameters:
        - data: The data to be stored in the new node.
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
obj = DeleteAtGivenPosition()
obj.insert(5)
obj.insert(100)
obj.insert(110)
obj.insert(700)
obj.insert(61)
obj.insert(26)
obj.insert(500)
obj.traverse()
obj.delete_after_given_position(2)
obj.traverse()

"""
Output:
    5->100->110->700->61->26->500->
    5->100->110->61->26->500->
"""
