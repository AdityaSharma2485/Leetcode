class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])  # Sort jobs by end time
        n = len(jobs)
        
        dp = [0] * (n + 1)  # Dynamic programming array to store maximum profit
        
        for i in range(1, n + 1):
            current_profit = jobs[i - 1][2]  # Profit of current job
            start_time = jobs[i - 1][0]  # Start time of current job
            
            # Binary search to find the latest job that finishes before the start time of the current job
            left, right = 0, i - 1
            while left <= right:
                mid = left + (right - left) // 2
                if jobs[mid][1] <= start_time:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Update maximum profit considering whether to include the current job or not
            include_profit = current_profit + dp[left]
            dp[i] = max(include_profit, dp[i - 1])
        
        return dp[n]
