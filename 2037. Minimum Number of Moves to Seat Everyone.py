class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort the seats and students arrays
        seats.sort()
        students.sort()
        
        # Initialize total moves counter
        total_moves = 0
        
        # Compute the total moves required
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
        
        return total_moves
