class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # Move the lighter person to the next available position
            right -= 1  # Move the heavier person to the next available position
            boats += 1
        
        return boats
        
