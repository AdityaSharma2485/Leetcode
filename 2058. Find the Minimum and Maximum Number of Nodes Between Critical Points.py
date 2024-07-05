# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # Positions of critical points
        critical_points = []
        current = head
        position = 0
        
        while current and current.next and current.next.next:
            prev_val = current.val
            curr_val = current.next.val
            next_val = current.next.next.val
            
            if (curr_val > prev_val and curr_val > next_val) or (curr_val < prev_val and curr_val < next_val):
                critical_points.append(position + 1)
            
            current = current.next
            position += 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]
        
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        
        return [min_distance, max_distance]
