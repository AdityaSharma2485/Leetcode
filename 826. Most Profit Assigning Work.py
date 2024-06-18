class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        # Combine jobs' difficulty and profit, then sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort workers by their ability
        worker.sort()
        
        max_profit = 0
        total_profit = 0
        i = 0
        n = len(jobs)
        
        for ability in worker:
            # Update the maximum profit we can get for the current ability
            while i < n and jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            # Add the best profit for this worker
            total_profit += max_profit
        
        return total_profit
