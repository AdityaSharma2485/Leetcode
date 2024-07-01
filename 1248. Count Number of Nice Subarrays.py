class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Convert nums to 1s (for odd numbers) and 0s (for even numbers)
        odd = [0] * len(nums)
        for i in range(len(nums)):
            odd[i] = 1 if nums[i] % 2 == 1 else 0
        
        # Initialize a prefix sum hashmap
        prefix_sum_count = {0: 1}
        current_sum = 0
        nice_subarrays = 0
        
        for num in odd:
            current_sum += num
            if current_sum - k in prefix_sum_count:
                nice_subarrays += prefix_sum_count[current_sum - k]
            
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1
        
        return nice_subarrays
