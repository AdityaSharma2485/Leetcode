from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair capital and profits together and sort by capital required
        projects = list(zip(capital, profits))
        projects.sort()
        
        max_heap = []
        current = 0
        n = len(projects)
        
        for _ in range(k):
            # Push all projects that can be started with the current capital into the max heap
            while current < n and projects[current][0] <= w:
                heapq.heappush(max_heap, -projects[current][1])  # use negative to simulate max-heap
                current += 1
            
            # If we can't start any more projects, break the loop
            if not max_heap:
                break
            
            # Select the project with the maximum profit
            w += -heapq.heappop(max_heap)
        
        return w

        
