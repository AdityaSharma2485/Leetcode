class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict

        # Step 1: Calculate the degree of each city
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1

        # Step 2: Sort cities by their degree in descending order
        city_degree_pairs = [(degree[i], i) for i in range(n)]
        city_degree_pairs.sort(reverse=True)

        # Step 3: Assign values based on sorted order
        value_assignment = [0] * n
        current_value = n
        for _, city in city_degree_pairs:
            value_assignment[city] = current_value
            current_value -= 1

        # Step 4: Calculate the total importance of all roads
        total_importance = 0
        for road in roads:
            total_importance += value_assignment[road[0]] + value_assignment[road[1]]

        return total_importance
