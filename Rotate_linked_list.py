"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        length, last_position = 1, head
        
        while last_position.next:
            length += 1
            last_position = last_position.next

        
        k = k % length
        if not k:
            return head

        count = 1
        position = length - k 
        pointer = head
        while count < position:
            pointer = pointer.next
            count += 1
        
        last_position.next = head
        head = pointer.next 
        pointer.next = None
        return head 
             
