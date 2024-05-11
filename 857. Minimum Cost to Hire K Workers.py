import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        # Pair each worker's quality with their minimum wage 
        # and sort the workers based on their wage-to-quality ratio.
        workers = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
      
        # Initialize the answer as infinity to be later minimized
        # Initialize the total quality of workers hired so far as zero
        min_cost = float('inf')
        total_quality = 0
      
        # Max heap to store the negative of qualities, 
        # since heapq in Python is a min heap by default
        max_heap = []
      
        # Iterate over each worker
        for q, w in workers:
            # Add the current worker's quality to the total quality
            total_quality += q
            # Push the negative quality to the heap
            heapq.heappush(max_heap, -q)
          
            # If we have more than k workers, remove the one with the highest quality
            if len(max_heap) > k:
                # Since we stored negative qualities, popping from heap retrieves
                # and removes the biggest quality from the total
                total_quality += heapq.heappop(max_heap)
          
            # If we've collected a group of k workers
            if len(max_heap) == k:
                # Calculate the current cost for this group of workers, which is
                # the wage-to-quality ratio of the current worker times total quality
                # and update the minimum cost if it's less than the previous minimum
                min_cost = min(min_cost, w / q * total_quality)
      
        # Return the minimum cost found to hire k workers
        return min_cost
