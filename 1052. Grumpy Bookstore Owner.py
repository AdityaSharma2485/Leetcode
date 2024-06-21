class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        # Total satisfied customers without using the technique
        total_satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        
        # Additional customers satisfied when using the technique
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        
        # Calculate the additional satisfied customers for the first 'minutes' window
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
        
        max_additional_satisfied = current_additional_satisfied
        
        # Slide the window across the rest of the customers
        for i in range(minutes, len(customers)):
            if grumpy[i - minutes] == 1:
                current_additional_satisfied -= customers[i - minutes]
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            
            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
        
        return total_satisfied + max_additional_satisfied
