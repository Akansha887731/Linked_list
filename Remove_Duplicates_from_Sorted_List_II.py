"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
 
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        prev = ListNode(next = head)
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                duplicate = curr.val
                while curr and curr.val == duplicate:
                    if curr == head :
                        head = head.next
                    t1 = curr
                    curr = curr.next
                    t1.next = None
                    prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return head
