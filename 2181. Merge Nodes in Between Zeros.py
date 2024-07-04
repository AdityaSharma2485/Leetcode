# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        # Initialize pointers
        current = head.next  # Skip the initial zero
        new_list_head = ListNode(0)  # Dummy node for the new list
        new_list_tail = new_list_head  # Pointer to the tail of the new list

        sum_segment = 0

        while current is not None:
            if current.val == 0:
                # End of a segment
                new_node = ListNode(sum_segment)
                new_list_tail.next = new_node
                new_list_tail = new_node  # Move the tail
                sum_segment = 0  # Reset the sum for the next segment
            else:
                # Sum the values between zeros
                sum_segment += current.val
            
            current = current.next  # Move to the next node

        return new_list_head.next  # Skip the dummy node and return the new list head
