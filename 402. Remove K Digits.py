class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        # Iterate through each digit in the number
        for digit in num:
            # While the stack is not empty, k is greater than 0,
            # and the current digit is less than the top digit of the stack
            while stack and k > 0 and digit < stack[-1]:
                # Pop the top digit from the stack
                stack.pop()
                # Decrement k
                k -= 1
            
            # Push the current digit onto the stack
            stack.append(digit)
        
        # Remove remaining digits if k is greater than 0
        while k > 0:
            stack.pop()
            k -= 1
        
        # Construct the smallest possible number from the digits remaining in the stack
        smallest_num = ''.join(stack).lstrip('0')
        
        # If the resulting number is empty, return '0'
        if not smallest_num:
            return '0'
        
        return smallest_num
