class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current_position = 1
        forward_direction = True
        
        for _ in range(time):
            if forward_direction:
                current_position += 1
                if current_position > n:
                    current_position = n - 1
                    forward_direction = False
            else:
                current_position -= 1
                if current_position < 1:
                    current_position = 2
                    forward_direction = True
        
        return current_position
