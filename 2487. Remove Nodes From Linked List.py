# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # Function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Reverse the linked list
        head = reverseLinkedList(head)
        
        max_value = head.val
        prev = head
        current = head.next
        
        while current:
            if current.val < max_value:
                # Remove the current node
                prev.next = current.next
            else:
                # Update the maximum value
                max_value = current.val
                prev = current
            current = prev.next
        
        # Reverse the modified linked list back
        return reverseLinkedList(head)
