"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        position = length - n + 1

        if position == 1:
            prev = head
            head = head.next
            prev.next = None
            return head

        count = 1
        current = head
        while count < position - 1:
            count += 1
            current = current.next
            
        node_to_delete = current.next
        current.next = node_to_delete.next
        node_to_delete.next = None
        return head
