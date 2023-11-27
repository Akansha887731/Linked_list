"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):    

        if left == right:
            return head
        
        t1 = head
        t_prev = None
        t_curr = None
        t_tail = None 

        for count in range(1, right+ 1):
            if count == left - 1:
                t_prev = t1
            if count == left:
                t_curr = t1
            if count == right and t1.next:
                t_tail = t1.next
            t1 = t1.next
        
        prev = t_curr
        curr = t_curr.next      
        while curr != t_tail:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        if t_prev:
            t_prev.next = prev
        else:
            head = prev

        t_curr.next = t_tail 

        return head
