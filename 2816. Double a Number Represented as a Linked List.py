# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Function to reverse a linked list and double its value
        def doubleAndReverse(node):
            carry = 0
            while node:
                node.val = node.val * 2 + carry
                carry = node.val // 10
                node.val %= 10
                prev = node
                node = node.next
            if carry:
                prev.next = ListNode(carry)
            return reverseLinkedList(head)
        
        # Reverse the given linked list
        head = reverseLinkedList(head)
        
        # Double the value of each node and reverse the list again
        return doubleAndReverse(head)
